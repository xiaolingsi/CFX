from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .Stage import Stage

@dataclass_json
@dataclass
class RecipeStageInformation:
    """** NOTE: ADDED in CFX 1.2 **
    Describes some information about a recipe for a specific  stage"""
    
    # A structure describing basic information about the stage.
    Stage: Optional[Stage] = None
    
    # The total amount of time (in ms) that is expected to process one unit or group of units (as in the case of a carrier or panelized PCB) for a stage of the machine, 
    # assuming no blocked or starved conditions at the station. This includes both productive and non-productive time, such as transfer, 
    # positioning, etc.
    ExpectedCycleTime: float = 0.0
    
    # ** NOTE: ADDED in CFX 1.6 **
    # The total amount of productive time (in ms) that is expected to process one unit or group of units (as in the case of a carrier or panelized PCB),
    # assuming no blocked or starved conditions at the station. This does not include any non-productive time, such as transfer, positioning, etc.
    ExpectedWorkTime: Optional[float] = None
    
    # The number of components to install for each unit of a work for a stage of the machine.
    NumberOfComponentsPerUnit: float = 0.0