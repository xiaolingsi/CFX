import asyncio
import gzip
import io
import json
import threading
import time
import uuid

from proton import int32, Sender, Message
from proton.reactor import Container

from Amqp.CFXEndpoint import CFXEndpoint
from CFX.CFXEnvelope import CFXEnvelope
from CFX.CFXUtils import CFXUtils
from CFX.Messages.CoreCommunication.HeartBeat import HeartBeat


class CFXContainer(object):
    def __init__(self, cfx_endpoint: CFXEndpoint,debug_info = False):
        self.cfx_endpoint: CFXEndpoint = cfx_endpoint
        self.cfx_handle = self.cfx_endpoint.cfx_handle
        self.container = Container(self.cfx_endpoint)
        self.container_thread_handler = None
        self.sender_list = list()
        self.request_senders = dict()
        self.response_receivers = dict()
        self.linked_queues = dict()
        self.heartbeat_frequency = 60
        self.heartbeat_task = None
        self.debug_info = debug_info
        self.log_utils = CFXUtils()

    def set_heartbeat_frequency(self, frequency):
        self.heartbeat_frequency = frequency

    def send_heartbeat(self):
        if not self.heartbeat_frequency:
            self.heartbeat_frequency = 60
        if self.heartbeat_frequency == 0:
            return
        while True:
            for each_sender in self.sender_list:
                heartBeat_msg = CFXEnvelope(source=self.cfx_handle,
                                            message_body=HeartBeat(self.cfx_handle, self.heartbeat_frequency)).to_json()
                gzip_msg = gzip.compress(json.dumps(heartBeat_msg).encode("utf-8"))
                heartBeat = Message(content_encoding="gzip",
                                    content_type='application/json;charset="utf-8"',
                                    inferred=True,
                                    reply_to=self.cfx_handle, durable=True,
                                    priority=4, id=str(uuid.uuid4()),
                                    properties={'cfx-topic': 'CFX',
                                                'cfx-message': 'CFX.Heartbeat',
                                                'cfx-handle': self.cfx_handle,
                                                'cfx-target': None},
                                    body=gzip_msg)
                each_sender.send(heartBeat)
                if self.debug_info:
                    self.log_utils.info_log("Publish heartbeat")
            time.sleep(self.heartbeat_frequency)

    def open_endpoint(self):
        self.container_thread_handler = threading.Thread(target=self.container.run)
        self.container_thread_handler.start()
        threading.Thread(target=self.send_heartbeat).start()

    def add_publish_channel(self, target_url, target_listener):
        add_sender: Sender = self.container.create_sender(target_url + "/" + target_listener)
        self.sender_list.append(add_sender)
        if self.debug_info:
            self.log_utils.info_log("Add publish channel: " + target_url + "/" + target_listener)

    def publish_msg(self, msg: CFXEnvelope):
        msg.Source = self.cfx_handle
        for each_sender in self.sender_list:
            gzip_msg = gzip.compress(json.dumps(msg.to_json()).encode("utf-8"))
            amqp_msg = Message(content_encoding="gzip", content_type='application/json;charset="utf-8"', inferred=True,
                               reply_to='', durable=True, priority=4, id=str(uuid.uuid4()),
                               properties={'cfx-topic': msg.MessageName.rsplit(".", 1)[0],
                                           'cfx-message': msg.MessageName,
                                           'cfx-handle': self.cfx_handle,
                                           'cfx-target': None}, body=gzip_msg)
            each_sender.send(amqp_msg)
        if self.debug_info:
            self.log_utils.info_log("Publish message: " + msg.MessageName)

    async def execute_request(self, target_url, target_handle, request: CFXEnvelope = None):
        link_id = target_url + "WmhhbmdLZVhpbgp4aWFvbGluZ3NpOTVAZ21haWwuY29t" + target_handle
        if link_id not in self.request_senders:
            link_queue = self.cfx_handle + "_WmhhbmdLZVhpbgp4aWFvbGluZ3NpOTVAZ21haWwuY29t_" + str(uuid.uuid4())
            request_sender = self.container.create_sender(target_url,
                                                          name=link_queue,
                                                          source=None,
                                                          target=target_handle)  # 发送request
            response_receiver = self.container.create_receiver(target_url,
                                                               target=link_queue,
                                                               source=target_handle,
                                                               dynamic=False,
                                                               name="request-receiver"
                                                               )  # 接收response
            self.linked_queues[link_id] = link_queue
            self.request_senders[link_id] = request_sender
            self.response_receivers[link_id] = response_receiver
        request_id = "REQUEST-" + str(uuid.uuid4())
        request.Source = self.cfx_handle
        request.Target = target_handle
        request.to_json()
        this = gzip.compress(json.dumps(request.to_json()).encode("utf-8"))
        msg = Message(content_encoding="gzip",
                      content_type='application/json;charset="utf-8"',
                      inferred=True,
                      address=target_handle,
                      reply_to=self.linked_queues[link_id],
                      durable=True, priority=4, id=request_id,
                      correlation_id=request_id,
                      properties={'offset': int32(1)}, body=this)
        self.request_senders[link_id].send(msg)
        if self.debug_info:
            self.log_utils.info_log("Execute Request: " + request.MessageName)
        try:
            response = await asyncio.wait_for(self.wait_for_response(request_id), timeout=30.0)
            if self.debug_info:
                self.log_utils.info_log("Receive Response: " + response)
            return response
        except asyncio.TimeoutError:
            self.log_utils.error_log("request time out: " + request.MessageName)

    async def wait_for_response(self, request_id):
        while request_id not in self.cfx_endpoint.rr_match:
            await asyncio.sleep(0.1)
        response: Message = self.cfx_endpoint.rr_match[request_id]
        del self.cfx_endpoint.rr_match[request_id]
        if response.content_encoding == "gzip":
            with gzip.GzipFile(fileobj=io.BytesIO(response.body.tobytes())) as f:
                decompressed_data = f.read()
        else:
            decompressed_data = response.body.tobytes()
        return decompressed_data.decode("utf-8")

    def close_endpoint(self):
        self.container.stop()
        self.container_thread_handler.join()
        self.container_thread_handler = None
        self.sender_list.clear()
        self.request_senders.clear()
        self.response_receivers.clear()
        self.linked_queues.clear()
        self.cfx_endpoint.rr_match.clear()
        self.cfx_endpoint.acceptor.close()
        self.cfx_endpoint.acceptor = None
        self.cfx_endpoint.senders.clear()
