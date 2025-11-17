"""
A specialized type of Activity that occurs when a unit is under placement
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from ..Activity import Activity
from ..ValueAddType import ValueAddType
from .SMTPlacementType import SMTPlacementType
from .SMTHeadInformation import SMTHeadInformation


@dataclass_json
@dataclass
class SMTPlacementActivity(Activity):
    """
    A specialized type of Activity that occurs when a unit is under placement
    """
    
    # The type of placement for this activity
    PlacementType: SMTPlacementType = SMTPlacementType.Automatic
    
    # The Heads used for the placement
    Heads: List[SMTHeadInformation] = field(default_factory=list)
    
    def __post_init__(self):
        # Set default values for Activity base class
        if not self.ActivityName:
            self.ActivityName = "PLACEMENT"
        if not self.ValueAddType:
            self.ValueAddType = ValueAddType.RealValueAdd