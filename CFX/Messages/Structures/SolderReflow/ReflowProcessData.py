"""
Provides information about conditions within a reflow oven at a given point in time.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from ..ProcessData import ProcessData
from .ReflowZoneData import ReflowZoneData


@dataclass_json
@dataclass
class ReflowProcessData(ProcessData):
    """
    Provides information about conditions within a reflow oven at a given point in time.
    """
    
    # The speed (in cm / minute) of conveyor
    ConveyorSpeed: float = 0.0
    
    # The converyor speed setpoint (in cm / minute)
    ConveyorSpeedSetpoint: float = 0.0
    
    # Process data (temperatures, etc.) for each zone of the reflow oven at the 
    # time when this transaction took place.
    ZoneData: List[ReflowZoneData] = field(default_factory=list)

    type: str = "CFX.Structures.SolderReflow.ReflowProcessData, CFX"

    def __init__(self,zone_data:List[ReflowZoneData]=None):
        self.type = "CFX.Structures.SolderReflow.ReflowProcessData, CFX"
        self.ZoneData = zone_data or []

