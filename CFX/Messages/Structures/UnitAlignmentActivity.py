from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .Activity import Activity
from .ValueAddType import ValueAddType


@dataclass_json
@dataclass
class UnitAlignmentActivity(Activity):
    """
    A specialized type of Activity that occurs when a unit is aligned (located / positioned) within a stage
    of an endpoint prior to the commencement of work.
    """
    
    # The amount of correction applied in the X axis, express in millimeters (mm)
    DX: float = 0.0
    
    # The amount of correction applied in the Y axis, express in millimeters (mm)
    DY: float = 0.0
    
    # The amount of correction applied in the Z axis, express in millimeters (mm)
    DZ: float = 0.0
    
    # The counter-clockwise rotational correction applied in the X-Y plane (in degrees)
    DXY: float = 0.0
    
    # The counter-clockwise rotational correction applied in the Z-X plane (in degrees)
    DZX: float = 0.0
    
    # The counter-clockwise rotational correction applied in the Z-Y plane (in degrees)
    DZY: float = 0.0
    
    def __post_init__(self):
        """Set default values after initialization"""
        self.ActivityName = "UNIT ALIGNMENT"
        self.ValueAddType = ValueAddType.NonValueAdd