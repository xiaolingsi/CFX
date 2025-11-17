"""
Structure defining the parameters for a particular zone within a solder reflow oven.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from .ReflowZone import ReflowZone
from .ReflowSetPoint import ReflowSetPoint


@dataclass_json
@dataclass
class ReflowZoneParameter:
    """
    Structure defining the parameters for a particular zone within a solder reflow oven.
    """
    
    # The related Zone (Stage)
    Zone: ReflowZone = field(default_factory=lambda: ReflowZone())
    
    # A list of setpoints of varying types for each sub-area within this zone.
    Setpoints: List[ReflowSetPoint] = field(default_factory=list)