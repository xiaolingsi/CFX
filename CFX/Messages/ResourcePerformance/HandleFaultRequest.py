import uuid
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class HandleFaultRequest(CFXMessage):
    FaultOccurrenceId: uuid.UUID = field(default_factory=uuid.uuid4)
    HandleRemote: bool = False

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, handle_remote=False, fault_occurrence_id=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.HandleFaultRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.HandleFaultRequest"
        self.FaultOccurrenceId = fault_occurrence_id if fault_occurrence_id is not None else uuid.uuid4()
        self.HandleRemote = handle_remote



