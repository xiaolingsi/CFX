from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json
from .Stage import Stage
from .MaterialSetupRequirement import MaterialSetupRequirement
from .ToolSetupRequirement import ToolSetupRequirement


@dataclass_json
@dataclass
class StationSetupRequirements:
    """
    Describes the material setup requirements for a particular process endpoint to perform a 
    particular operation on one or more partiuclar products.  Also includes information on
    where specifically the materials should be loaded (when applicable), AML (where applicable),
    and alternate part information (where applicable).
    """
    
    # The production lane to which this setup applies (when applicable)
    Lane: Optional[int] = None
    
    # The stage to which this setup applies (when applicable)
    Stage: Optional[Stage] = None
    
    # An optional name for this particular setup
    SetupName: str = ""
    
    # A list of the materials that need to be installed / loaded at the process endpoint
    # to perform a particular process.
    MaterialSetupRequirements: List[MaterialSetupRequirement] = field(default_factory=list)
    
    # A list of the tools (heads, nozzels, hammers, wrenches, etc.) that need to be installed / loaded at the 
    # process endpoint to perform a particular process.
    ToolSetupRequirements: List[ToolSetupRequirement] = field(default_factory=list)