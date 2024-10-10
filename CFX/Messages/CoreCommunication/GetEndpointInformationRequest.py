from abc import ABC

from CFX.CFXMessage import CFXMessage


class GetEndpointInformationRequest(CFXMessage):

    def __init__(self, cfx_handle):
        super().__init__()
        self.type = "CFX.GetEndpointInformationRequest,CFX"
        self.message_name = "CFX.GetEndpointInformationRequest"
        self.CFXHandle = cfx_handle

    def to_cfx_json(self):
        return {
            "$type": self.type,
            "CFXHandle": self.CFXHandle
        }
