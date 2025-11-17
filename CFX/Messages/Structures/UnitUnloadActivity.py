from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .Activity import Activity
from .ValueAddType import ValueAddType


@dataclass_json
@dataclass
class UnitUnloadActivity(Activity):
    """
    A specialized type of Activity that occurs when a unit is unloaded from an endpoint.
    """
    
    # The total amount of time consumed by the load event.
    UnloadTime: float = 0.0
    
    def __post_init__(self):
        """Set default values after initialization"""
        self.ActivityName = "UNIT UNLOAD"
        self.ValueAddType = ValueAddType.NonValueAdd