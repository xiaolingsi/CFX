from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.Stage import Stage


@dataclass_json
@dataclass
class ChangeSleepStateResponse(CFXMessage):
    """
    Response to an external source to modify a generic configuration parameter of a process endpoint.
    ** NOTE: ADDED in CFX 1.3 **
    """
    Result: RequestResult = field(default_factory=RequestResult)
    OldSleepState: str = "Awake"
    NewSleepState: str = "Awake"
    Stage: Optional[Stage] = None
    Lane: Optional[int] = None
    TransitionTimeRemaining: Optional[str] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result=None, old_sleep_state="Awake", new_sleep_state="Awake", 
                 stage=None, lane=0, transition_time_remaining=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.ChangeSleepStateResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.ChangeSleepStateResponse"
        self.Result = result if result is not None else RequestResult()
        self.OldSleepState = old_sleep_state
        self.NewSleepState = new_sleep_state
        self.Stage = stage
        self.Lane = lane
        self.TransitionTimeRemaining = transition_time_remaining