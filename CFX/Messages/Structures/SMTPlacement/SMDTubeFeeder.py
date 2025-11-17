"""
Describes and SMT Tube Feeder
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from ..MaterialCarrier import MaterialCarrier


@dataclass_json
@dataclass
class SMDTubeFeeder(MaterialCarrier):
    """
    Describes and SMT Tube Feeder
    """
    
    # The unique identifier of the vibratoryb tube feeder base of which this
    # tube feeder position is a member. If lanes are not specifically labeled,
    # both the UniqueIdentifer field and this property should be populated
    # with the same value.
    BaseUniqueIdentifier: str = ""
    
    # The friendly name of the tube feeder base.
    BaseName: str = ""
    
    # The position number of this tube feeder position within its base.
    LaneNumber: int = 0
    
    # The width of this lane within the tube feeder (in mm)
    Width: float = 0.0
    
    # The offset between this lane and the next adjacent lane in this tube feeder
    Pitch: float = 0.0