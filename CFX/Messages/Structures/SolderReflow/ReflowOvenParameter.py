"""
Dynamic Parameter structure containing the configurable parameters of a solder reflow oven.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from ..Parameter import Parameter
from .ReflowZoneParameter import ReflowZoneParameter


@dataclass_json
@dataclass
class ReflowOvenParameter(Parameter):
    """
    Dynamic Parameter structure containing the configurable parameters of a solder reflow oven.
    """
    
    # The desired conveyor speed, expressed in centimeters per minute (cm / min)
    ConveyorSpeedSetpoint: float = 0.0
    
    # The width of the conveyor, expressed in centimeters (cm)
    ConveyorWidth: float = 0.0
    
    # A list of the structures defining the parameters for each zone.
    ZoneParameters: List[ReflowZoneParameter] = field(default_factory=list)