import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Fault import Fault
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator

@dataclass_json
@dataclass
class FaultAcknowledged(CFXMessage):
    FaultOccurrenceId: uuid.uuid4
    Operator:Operator

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,operator,fault_occurrence_id = uuid.uuid4()):
        super().__init__()
        self.type = "CFX.ResourcePerformance.FaultAcknowledged,CFX"
        self.message_name = "CFX.ResourcePerformance.FaultAcknowledged"
        self.FaultOccurrenceId = fault_occurrence_id
        self.Operator = operator



