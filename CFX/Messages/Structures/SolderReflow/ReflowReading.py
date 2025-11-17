"""
Structure that describes setpoints and key actuals of a particular area
within a particular zone of a reflow oven.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional
from .ReflowSubZoneType import ReflowSubZoneType
from .ReflowReadingType import ReflowReadingType


@dataclass_json
@dataclass
class ReflowReading:
    """
    Structure that describes setpoints and key actuals of a particular area
    within a particular zone of a reflow oven.
    """
    
    # An enumeration that describes a particular area within a particular zone of a reflow oven.
    SubZone: ReflowSubZoneType = ReflowSubZoneType.Top
    
    # An enumeration describing the type of reading.
    ReadingType: ReflowReadingType = ReflowReadingType.Temperature
    
    # The value of reading (expressed in the appropriate units for ReadingType).
    ReadingValue: Optional[float] = None