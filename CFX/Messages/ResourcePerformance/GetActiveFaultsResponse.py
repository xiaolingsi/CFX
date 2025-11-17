from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Fault import Fault
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class GetActiveFaultsResponse(CFXMessage):
    Result: RequestResult = field(default_factory=RequestResult)
    ActiveFaults: List[Fault] = field(default_factory=list)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result=None, active_faults=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.GetActiveFaultsResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.GetActiveFaultsResponse"
        self.Result = result if result is not None else RequestResult()
        self.ActiveFaults = active_faults if active_faults is not None else []

    def add_fault(self, fault: Fault):
        self.ActiveFaults.append(fault)


