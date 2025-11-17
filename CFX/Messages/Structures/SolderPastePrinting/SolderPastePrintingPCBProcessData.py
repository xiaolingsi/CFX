"""
** NOTE: ADDED in CFX 1.2 **
The new Process Data for the PCB processed.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from datetime import timedelta
from ..ProcessData import ProcessData
from .Stroke import Stroke
from .Separation import Separation
from .PeriodicCleaning import PeriodicCleaning


@dataclass_json
@dataclass
class SolderPastePrintingPCBProcessData(ProcessData):
    """
    ** NOTE: ADDED in CFX 1.2 **
    The new Process Data for the PCB processed.
    """
    
    # List of Stroke objects for Solder Paste Printing PCB Process Data
    Strokes: List[Stroke] = field(default_factory=list)
    
    # Separation object 
    Separation: Optional[Separation] = None
    
    # Periodic cleaning object List. Normally it shall be one, but in this way it may be extended more easily 
    PeriodicCleanings: List[PeriodicCleaning] = field(default_factory=list)
    
    # Recipe name for the process data
    RecipeName: Optional[str] = None
    
    # Printing offset on the X-Axis
    OffsetX: Optional[float] = None
    
    # Printing offset on the Y-Axis
    OffsetY: Optional[float] = None
    
    # Printing offset on the Theta-Axis
    OffsetTheta: Optional[float] = None
    
    # First direction of the Printing process
    FirstPrintDirection: Optional[str] = None
    
    # Cycle time for the Printing process, in the format hh:mm:ss.fffffff
    CycleTime: Optional[timedelta] = None