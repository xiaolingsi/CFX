from CFX.CFXMessage import CFXMessage
from CFX.Messages.UnitPojo.Stage import Stage
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StatusResult import StatusResult


@dataclass_json
@dataclass
class HandleFaultResponse(CFXMessage):
    Result: RequestResult

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,result):
        super().__init__()
        self.type = "CFX.ResourcePerformance.HandleFaultResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.HandleFaultResponse"
        self.Result = result


if __name__ == '__main__':
    request_result = RequestResult(StatusResult.Success, 0, "Success")
    resp = HandleFaultResponse(result=request_result)
    print(resp.to_cfx_json())

