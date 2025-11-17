from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class ChangeSleepStateRequest(CFXMessage):
    """
    This request allows an external source to change the sleep state of a Stage or Station.
    ** NOTE: ADDED in CFX 1.3 **
    """
    stage_name: Optional[str] = None
    new_sleep_state: Optional[str] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, stage_name=None, new_sleep_state=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.ChangeSleepStateRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.ChangeSleepStateRequest"
        self.stage_name = stage_name
        self.new_sleep_state = new_sleep_state