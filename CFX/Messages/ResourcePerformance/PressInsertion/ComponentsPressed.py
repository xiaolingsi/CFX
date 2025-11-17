from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils


@dataclass_json
@dataclass
class ComponentsPressed(CFXMessage):
    """
    Sent periodically by a Press Fit machine to indicate the number of presses which were
    successfully or unsuccessfully completed during the sample time window.
    """
    start_time: str = field(default_factory=CFXUtils.get_iso8601_time)
    end_time: str = field(default_factory=CFXUtils.get_iso8601_time)
    total_components_pressed: int = 0
    total_components_not_pressed: int = 0

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, start_time=None, end_time=None, total_components_pressed=0, total_components_not_pressed=0):
        super().__init__()
        self.type = "CFX.ResourcePerformance.PressInsertion.ComponentsPressed,CFX"
        self.message_name = "CFX.ResourcePerformance.PressInsertion.ComponentsPressed"
        self.start_time = start_time if start_time is not None else CFXUtils.get_iso8601_time()
        self.end_time = end_time if end_time is not None else CFXUtils.get_iso8601_time()
        self.total_components_pressed = total_components_pressed
        self.total_components_not_pressed = total_components_not_pressed