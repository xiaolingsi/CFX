from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..Measurement import Measurement

@dataclass_json
@dataclass
class OffsetMeasurement(Measurement):
    """Describes the results of measurements that were made on the position of a specific PCB component."""
    
    # The x offset of the component from center (in mm)
    DX: float = 0.0
    
    # The y offset of the component from center (in mm)
    DY: float = 0.0
    
    # The z offset of the component from level (in mm)
    DZ: float = 0.0
    
    # The counter-clockwise rotational offset on the X-Y plane (in degrees)
    RXY: float = 0.0
    
    # The counter-clockwise rotational offset on the Z-X plane (in degrees)
    RZX: float = 0.0
    
    # The counter-clockwise rotational offset on the Z-Y plane (in degrees)
    RZY: float = 0.0