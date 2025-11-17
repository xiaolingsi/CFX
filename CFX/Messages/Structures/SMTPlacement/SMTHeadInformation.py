"""
Describes a head for an endpoint that is an SMT placement machine.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from ..HeadInformation import HeadInformation
from .SMTHeadType import SMTHeadType


@dataclass_json
@dataclass
class SMTHeadInformation(HeadInformation):
    """
    Describes a head for an endpoint that is an SMT placement machine.
    """
    
    # An enumeration indicating to purpose of this particular head
    SMTHeadType: SMTHeadType = SMTHeadType.Turret
    
    # Indicates to number of nozzle locations
    NumberOfNozzleLocations: int = 0
    
    # The accuracy of this head, expressed in mm. For example, a head that can accurately
    # place components to 1 micron would have accuracy of 0.001 mm.
    PlacementAccuracy: float = 0.0