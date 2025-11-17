from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage


@dataclass_json
@dataclass
class SleepStateChanged(CFXMessage):
    """
    Sent by a process endpoint when the sleep state transitions from one state to another.
    ** NOTE: ADDED in CFX 1.3 **
    """
    OldSleepState: str = "Awake"
    NewSleepState: str = "Awake"
    Stage: Optional[Stage] = None
    Lane: Optional[int] = None
    TransitionTimeRemaining: Optional[str] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, OldSleepState="Awake", NewSleepState="Awake", Stage=None, Lane=None, TransitionTimeRemaining=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.SleepStateChanged,CFX"
        self.message_name = "CFX.ResourcePerformance.SleepStateChanged"
        self.OldSleepState = OldSleepState
        self.NewSleepState = NewSleepState
        self.Stage = Stage
        self.Lane = Lane
        self.TransitionTimeRemaining = TransitionTimeRemaining or "00:00:00"