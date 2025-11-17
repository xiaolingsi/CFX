"""
A data structure describing set point for a particular area within a zone of a solder reflow oven.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional
from .ReflowSubZoneType import ReflowSubZoneType
from .ReflowSetpointType import ReflowSetpointType


@dataclass_json
@dataclass
class ReflowSetPoint:
    """
    A data structure describing set point for a particular area within a zone of a solder reflow oven.
    """
    
    # The area within zone to which setpoint applies.
    SubZone: ReflowSubZoneType = ReflowSubZoneType.Top
    
    # An enumeration describing the type of setpoint.
    SetpointType: ReflowSetpointType = ReflowSetpointType.Temperature
    
    # The nominal, target value of this setpoint.
    Setpoint: Optional[float] = None