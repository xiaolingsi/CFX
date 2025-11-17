from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Fault import Fault
from CFX.Messages.Structures.ResourceState import ResourceState


@dataclass_json
@dataclass
class StationStateChanged(CFXMessage):
    NewState: ResourceState = field(default_factory=lambda: ResourceState.SBY_NoProduct)
    OldState: ResourceState = field(default_factory=lambda: ResourceState.SBY_NoProduct)
    OldStateDuration: Optional[str] = None
    RelatedFault: Optional[Fault] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, old_state_duration=None, new_state=None, old_state=None, related_fault=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.StationStateChanged,CFX"
        self.message_name = "CFX.ResourcePerformance.StationStateChanged"
        self.OldStateDuration = old_state_duration
        self.NewState = new_state if new_state is not None else ResourceState.SBY_NoProduct
        self.OldState = old_state if old_state is not None else ResourceState.SBY_NoProduct
        self.RelatedFault = related_fault


