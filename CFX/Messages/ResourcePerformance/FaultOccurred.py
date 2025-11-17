from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Fault import Fault


@dataclass_json
@dataclass
class FaultOccurred(CFXMessage):
    Fault: Fault = field(default_factory=Fault)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, fault=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.FaultOccurred,CFX"
        self.message_name = "CFX.ResourcePerformance.FaultOccurred"
        self.Fault = fault if fault is not None else Fault()
