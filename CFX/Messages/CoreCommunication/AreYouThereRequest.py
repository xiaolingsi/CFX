from abc import ABC

from CFX.CFXMessage import CFXMessage


class AreYouThereRequest(CFXMessage):

    def __init__(self,cfx_handle):
        super().__init__()
        self.type = "CFX.AreYouThereRequest,CFX"
        self.message_name = "CFX.AreYouThereRequest"
        self.CFXHandle = cfx_handle

    def to_cfx_json(self):
        return {
            "$type": self.type,
            "CFXHandle": self.CFXHandle
        }
