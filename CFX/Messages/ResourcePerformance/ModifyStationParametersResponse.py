from CFX.CFXMessage import CFXMessage
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StatusResult import StatusResult


@dataclass_json
@dataclass
class ModifyStationParametersResponse(CFXMessage):
    Result: RequestResult

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,result):
        super().__init__()
        self.type = "CFX.ResourcePerformance.ModifyStationParametersResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.ModifyStationParametersResponse"
        self.Result = result




