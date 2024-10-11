from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Fault import Fault
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StatusResult import StatusResult


@dataclass_json
@dataclass
class GetActiveFaultsResponse(CFXMessage):
    Result: RequestResult
    ActiveFaults: list

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result):
        super().__init__()
        self.type = "CFX.ResourcePerformance.GetActiveFaultsResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.GetActiveFaultsResponse"
        self.Result = result
        self.ActiveFaults = list()

    def add_fault(self, fault: Fault):
        self.ActiveFaults.append(fault)


