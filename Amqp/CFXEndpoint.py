import gzip
import io
import json
import uuid
from abc import ABC

from proton import Message
from proton.handlers import MessagingHandler

from Amqp.CFXMessageImplements import CFXMessageImplements
from CFX.CFXUtils import CFXUtils
from CFX.CFXEnvelope import CFXEnvelope
from utils import logutils


class CFXEndpoint(MessagingHandler, CFXMessageImplements, ABC):
    def __init__(self, local_url, cfx_handle):
        super(CFXEndpoint, self).__init__()
        self.local_url = local_url
        self.cfx_handle = cfx_handle
        self.senders = {}
        self.acceptor = None
        self.rr_match = {}
        self.log_utils = logutils

    def on_start(self, event):
        self.acceptor = event.container.listen(self.local_url)  # 接收publish消息
        self.log_utils.info_log("Listen start at " + self.local_url)

    def on_link_opening(self, event):
        if event.link.is_sender:
            if event.link.remote_source and event.link.remote_source.dynamic:
                event.link.source.address = str(uuid.uuid4())
                self.senders[event.link.source.address] = event.link
            elif event.link.remote_target and event.link.remote_target.address:
                self.senders[event.link.remote_target.address] = event.link
            elif event.link.remote_source:
                event.link.source.address = event.link.remote_source.address
        elif event.link.remote_target:
            event.link.target.address = event.link.remote_target.address

    def on_message(self, event):
        sender = self.senders.get(event.message.reply_to)
        if not sender:
            if not event.message.correlation_id:
                if event.message.content_encoding == "gzip":
                    with gzip.GzipFile(fileobj=io.BytesIO(event.message.body.tobytes())) as f:
                        decompressed_data = f.read()
                else:
                    decompressed_data = event.message.body.tobytes()
                try:
                    self.on_message_receive_from_listener(json.loads(decompressed_data.decode("utf-8")))
                except Exception as e:
                    self.log_utils.error_log(e)
            else:
                self.rr_match[event.message.correlation_id] = event.message
        else:
            if event.message.content_encoding == "gzip":
                with gzip.GzipFile(fileobj=io.BytesIO(event.message.body.tobytes())) as f:
                    decompressed_data = f.read()
            else:
                decompressed_data = event.message.body.tobytes()
            try:
                resp = self.on_request_receive(json.loads(decompressed_data.decode("utf-8")))
            except Exception as e:
                self.log_utils.error_log(e)
                resp = None
            if isinstance(resp, CFXEnvelope):
                resp = resp.to_json()
            source = json.loads(decompressed_data)["Source"]
            if resp:
                resp["RequestID"] = event.message.correlation_id
                this = gzip.compress(json.dumps(resp).encode("utf-8"))
                msg = Message(address=event.message.reply_to,
                              correlation_id=event.message.correlation_id,
                              content_encoding="gzip",
                              content_type='application/json;charset="utf-8"',
                              inferred=True,
                              reply_to=source, durable=True, priority=4, id=str(uuid.uuid4()),
                              properties={'cfx-topic': resp["MessageName"].rsplit(".", 1)[0],
                                          'cfx-message': resp["MessageName"],
                                          'cfx-handle': self.cfx_handle,
                                          'cfx-target': source}, body=this)
            else:
                not_support_resp = {
                    "MessageName": "CFX.NotSupportedResponse",
                    "Version": "1.7",
                    "TimeStamp": CFXUtils.get_iso8601_time(),
                    "UniqueID": str(uuid.uuid4()),
                    "Source": self.cfx_handle, "Target": source,
                    "RequestID": event.message.correlation_id,
                    "MessageBody":
                        {
                            "$type": "CFX.NotSupportedResponse, CFX",
                            "RequestResult":
                                {
                                    "Result": "Success",
                                    "ResultCode": 0,
                                    "Message": None
                                }
                        }
                }
                this = gzip.compress(json.dumps(not_support_resp).encode("utf-8"))
                msg = Message(address=event.message.reply_to, correlation_id=event.message.correlation_id,
                              content_encoding="gzip", content_type='application/json;charset="utf-8"', inferred=True,
                              reply_to=source, durable=True, priority=4, id=str(uuid.uuid4()),
                              properties={'cfx-topic': "CFX",
                                          'cfx-message': "CFX.NotSupportedResponse",
                                          'cfx-handle': self.cfx_handle,
                                          'cfx-target': source}, body=this)
                self.log_utils.warning_log("NotSupportedResponse")
            sender.send(msg)
