"""
Describes an SMT Tape feeder.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from ..MaterialCarrier import MaterialCarrier


@dataclass_json
@dataclass
class SMDTapeFeeder(MaterialCarrier):
    """
    Describes an SMT Tape feeder.
    """
    
    # For multi-lane feeders, unique identifier of base. The UniqueIdentifier
    # property should be populated with unique identifer of specific lane
    # within feeder (if so labeled). If lanes are not specifically labeled, both
    # UniqueIdentifer and BaseUniqueIdentifier prooperties should be populated
    # with the same value.
    BaseUniqueIdentifier: str = ""
    
    # The friendly name of tape feeder base.
    BaseName: str = ""
    
    # For multi-lane tape feeders, this is the number of the position
    # of the lane within the feeder.
    LaneNumber: int = 1
    
    # The width of tape currently loaded on this feeder (in millimeters)
    TapeWidth: float = 0.0
    
    # The pitch (spacing between parts) of tape currently loaded on this feeder (in millimeters)
    TapePitch: float = 0.0