from CFX.CFXMessage import CFXMessage
from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StatusResult import StatusResult


class AreYouThereResponse(CFXMessage):
    def __init__(self, cfx_handle,RequestNetWorkUri,RequestTargetAddress):
        super().__init__()
        self.type = "CFX.AreYouThereResponse,CFX"
        self.message_name = "CFX.AreYouThereResponse"
        self.CFXHandle = cfx_handle
        self.RequestNetWorkUri = RequestNetWorkUri
        self.RequestTargetAddress = RequestTargetAddress
        self.Result = RequestResult(StatusResult.Success, 0, "Success")

    def to_cfx_json(self):
        return {
            "$type": self.type,
            "Result": self.Result.to_cfx_json(),
            "CFXHandle": self.CFXHandle,
            "RequestNetWorkUri": self.RequestNetWorkUri,
            "RequestTargetAddress": self.RequestTargetAddress
        }

