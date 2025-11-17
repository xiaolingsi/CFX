from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Segment:
    """
    An X/Y coordinate that is used to define a planar region.
    """
    
    # The X Coordinate
    X: float = 0.0
    
    # The Y Coordinate
    Y: float = 0.0