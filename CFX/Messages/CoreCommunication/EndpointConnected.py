from CFX.CFXMessage import CFXMessage


class EndpointConnected(CFXMessage):
    def __init__(self, cfx_handle,RequestNetWorkUri,RequestTargetAddress):
        super().__init__()
        self.type = "CFX.EndpointConnected,CFX"
        self.message_name = "CFX.EndpointConnected"
        self.CFXHandle = cfx_handle
        self.RequestNetWorkUri = RequestNetWorkUri
        self.RequestTargetAddress = RequestTargetAddress

    def to_cfx_json(self):
        return {
            "$type": self.type,
            "CFXHandle": self.CFXHandle,
            "RequestNetWorkUri": self.RequestNetWorkUri,
            "RequestTargetAddress": self.RequestTargetAddress
        }