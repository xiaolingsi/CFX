import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Fault import Fault
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class FaultCleared(CFXMessage):
    FaultOccurrenceId: uuid.uuid4
    Operator: Operator

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,operator, fault_occurrence_id = uuid.uuid4()):
        super().__init__()
        self.type = "CFX.ResourcePerformance.FaultCleared,CFX"
        self.message_name = "CFX.ResourcePerformance.FaultCleared"
        self.FaultOccurrenceId = fault_occurrence_id
        self.Operator = operator


if __name__ == '__main__':
    operator_ = Operator()
    fault_cleared = FaultCleared(operator=operator_)
    print(fault_cleared.to_cfx_json())