from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.Fault import Fault
from CFX.Messages.Structures.ResourceState import ResourceState


@dataclass_json
@dataclass
class StageStateChanged(CFXMessage):
    """
    Sent by a process endpoint when the production state of one of its stages transitions from one state to another.
    """
    Stage: Stage = None
    Lane: Optional[int] = None
    OldState: ResourceState = field(default_factory=lambda: ResourceState.SBY_NoProduct)
    OldStateDuration: Optional[str] = None
    NewState: ResourceState = field(default_factory=lambda: ResourceState.SBY_NoProduct)
    RelatedFault: Optional[Fault] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, Stage=None, Lane=None, OldState=None, OldStateDuration=None, NewState=None, RelatedFault=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.StageStateChanged,CFX"
        self.message_name = "CFX.ResourcePerformance.StageStateChanged"
        self.Stage = Stage
        self.Lane = Lane
        self.OldState = OldState if OldState is not None else ResourceState.SBY_NoProduct
        self.OldStateDuration = OldStateDuration
        self.NewState = NewState if NewState is not None else ResourceState.SBY_NoProduct
        self.RelatedFault = RelatedFault