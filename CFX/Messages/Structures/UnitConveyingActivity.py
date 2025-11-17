from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .Activity import Activity
from .ValueAddType import ValueAddType
from .Stage import Stage


@dataclass_json
@dataclass
class UnitConveyingActivity(Activity):
    """
    A specialized type of Activity that occurs when a unit is conveyed in an endpoint.
    """
    
    # The total distance of conveying (in mm)
    ConveyingDistance: float = 0.0
    
    # The Stage from where the unit is conveyed
    DepartureStage: Stage = None
    
    # The Stage to where the unit is conveyed
    ArrivalStage: Stage = None
    
    def __post_init__(self):
        """Set default values after initialization"""
        self.ActivityName = "UNIT CONVEYING"
        self.ValueAddType = ValueAddType.NonValueAdd