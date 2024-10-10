import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Fault import Fault
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class HandleFaultRequest(CFXMessage):
    FaultOccurrenceId: uuid.uuid4
    HandleRemote: bool

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, handle_remote:bool = False, fault_occurrence_id=uuid.uuid4()):
        super().__init__()
        self.type = "CFX.ResourcePerformance.HandleFaultRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.HandleFaultRequest"
        self.FaultOccurrenceId = fault_occurrence_id
        self.HandleRemote = handle_remote


if __name__ == '__main__':
    handleFaultRequest = HandleFaultRequest(handle_remote=True,fault_occurrence_id = uuid.uuid4())
    print(handleFaultRequest.to_cfx_json())
