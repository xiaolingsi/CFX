from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Fault import Fault
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class FaultOccurred(CFXMessage):
    Fault: Fault
    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,fault:Fault):
        super().__init__()
        self.type = "CFX.ResourcePerformance.FaultOccurred,CFX"
        self.message_name = "CFX.ResourcePerformance.FaultOccurred"
        self.Fault = fault



