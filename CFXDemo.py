import asyncio

from Amqp.CFXContainer import CFXContainer
from Amqp.CFXEndpoint import CFXEndpoint
from CFX.CFXEnvelope import CFXEnvelope
from CFX.CFXMessage import CFXMessage
from CFX.Messages.CoreCommunication import *
from CFX.Messages.Production import *
from CFX.Messages.InformationSystem import *
from CFX.Messages.ResourcePerformance import *
from utils import logutils


class MyCFXEndpoint(CFXEndpoint):
    def __init__(self, local_url, cfx_handle):
        super(MyCFXEndpoint, self).__init__(local_url, cfx_handle)
        self.log_utils = logutils

    def on_message_receive_from_listener(self, msg) -> None:
        self.log_utils.critical_log("Message receive from listener")
        self.log_utils.critical_log(msg)

    def on_request_receive(self, request) -> [dict, None, CFXMessage]:
        self.log_utils.critical_log("Request receive")
        self.log_utils.critical_log(request)
        if request["MessageName"] == "CFX.AreYouThereRequest":
            return CFXEnvelope(message_body=AreYouThereResponse(self.cfx_handle, self.local_url,self.cfx_handle))
        return None


async def main():
    endpoint = MyCFXEndpoint("127.0.0.1:16666", "OriHandle")
    container = CFXContainer(endpoint, debug_info=True)
    container.set_heartbeat_frequency(60)
    container.add_publish_channel("127.0.0.1:18888", "listener")

    container.open_endpoint()

    container.publish_msg(
        CFXEnvelope(message_body=EndpointConnected(endpoint.cfx_handle, endpoint.local_url, endpoint.cfx_handle))
    )

    resp = await container.execute_request("127.0.0.1:18888", "local", CFXEnvelope(message_body=AreYouThereRequest(endpoint.cfx_handle)))
    print(resp)


if __name__ == '__main__':
    asyncio.run(main())

