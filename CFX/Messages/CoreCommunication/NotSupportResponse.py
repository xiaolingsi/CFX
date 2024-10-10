from CFX.CFXMessage import CFXMessage
from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StatusResult import StatusResult


class NotSupportResponse(CFXMessage):
    def __init__(self):
        super().__init__()
        self.type = "CFX.NotSupportResponse,CFX"
        self.message_name = "CFX.NotSupportResponse"

    def to_cfx_json(self):
        return {
            "$type": self.type,
            "RequestResult": RequestResult(StatusResult.Success, 0, "Not Supported").to_json()
        }