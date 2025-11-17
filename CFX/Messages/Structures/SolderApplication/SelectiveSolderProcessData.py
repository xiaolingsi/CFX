"""
General data values that apply across the selective process cycle 
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from datetime import timedelta
from ..ProcessData import ProcessData


@dataclass_json
@dataclass
class SelectiveSolderProcessData(ProcessData):
    """
    General data values that apply across the selective process cycle 
    """
    
    # Result of the Selective Process
    # "Completed" or "Aborted"
    Process_Status: Optional[str] = None
    
    # The name of the active recipe at the time when the processing occurred.
    RecipeName: Optional[str] = None
    
    # Pressure od the incoming Nitrogen
    # in kPa (kilopascal)
    Nitrogen_Pressure: float = 0.0
    
    # Pressure od the incoming Air
    # in kPa (kilopascal)
    Air_Pressure: float = 0.0
    
    # The total number of parts processed
    # since the last reset of the Cycle Counter
    Cycle_Count: int = 0
    
    # The total time the item was within the Selective Soldering System
    Cycle_Time: Optional[timedelta] = None
    
    # The Purity of the incoming Nitrogen supply
    # in ppm (parts per million)
    Nitrogen_Purity: float = 0.0
    
    # The consumption of Nitrogen by the selective soldering system
    # in LPM (litres per minute)
    Nitrogen_Flow: float = 0.0
    
    # Fiducial correct enabled for the selective soldering system
    # "True" or "False"
    Fiducial_Enabled: bool = False