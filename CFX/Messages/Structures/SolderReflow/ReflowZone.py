"""
A specialized type of Stage that represents a thermal zone within a solder reflow oven.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from ..Stage import Stage
from .ReflowZoneType import ReflowZoneType


@dataclass_json
@dataclass
class ReflowZone(Stage):
    """
    A specialized type of Stage that represents a thermal zone within a solder reflow oven.
    """
    
    # The type/purpose of this zone.
    ReflowZoneType: ReflowZoneType = ReflowZoneType.PreHeat

    def __init__(self):
        super().__init__()
        self.ReflowZoneType = ReflowZoneType.PreHeat

