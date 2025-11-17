"""
Provides information about conditions of a particular zone of a reflow oven at a given point in time.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from .ReflowZone import ReflowZone
from .ReflowSetPoint import ReflowSetPoint
from .ReflowReading import ReflowReading


@dataclass_json
@dataclass
class ReflowZoneData:
    """
    Provides information about conditions of a particular zone of a reflow oven at a given point in time.
    """
    
    # Zone / Stage to which this reflow data is related.
    Zone: Optional[ReflowZone] = None
    
    # A list of current setpoints associated with this zone.
    Setpoints: List[ReflowSetPoint] = field(default_factory=list)
    
    # A list of readings / measurements that have been taken for this zone.
    Readings: List[ReflowReading] = field(default_factory=list)