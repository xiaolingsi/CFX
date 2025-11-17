from CFX.CFXMessage import CFXMessage


class EndpointShuttingDown(CFXMessage):
    def __init__(self, cfx_handle):
        super().__init__()
        self.type = "CFX.EndpointShuttingDown,CFX"
        self.message_name = "CFX.EndpointShuttingDown"
        self.CFXHandle = cfx_handle

    def to_cfx_json(self):
        return {
            "$type": self.type,
            "CFXHandle": self.CFXHandle
        }