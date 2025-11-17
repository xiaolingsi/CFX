import uuid
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class FaultCleared(CFXMessage):
    FaultOccurrenceId: uuid.UUID = field(default_factory=uuid.uuid4)
    Operator: Operator = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, operator=None, fault_occurrence_id=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.FaultCleared,CFX"
        self.message_name = "CFX.ResourcePerformance.FaultCleared"
        self.FaultOccurrenceId = fault_occurrence_id if fault_occurrence_id is not None else uuid.uuid4()
        self.Operator = operator


