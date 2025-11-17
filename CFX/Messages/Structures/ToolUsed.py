from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json
from .Tool import Tool
from .InstalledComponent import InstalledComponent


@dataclass_json
@dataclass
class ToolUsed:
    """
    A data structure representing an occurrence where a Tool is utilized when processing a specific production unit
    """
    
    # Unique ID of Production Unit, Panel, or Carrier
    UnitIdentifier: str = ""
    
    # Logical reference of production unit as defined by CFX position rule (see CFX standard section 5.6). 
    UnitPositionNumber: Optional[int] = None
    
    # A structure representing the Tool that was utilized
    Tool: Optional[Tool] = None
    
    # Indicates the number of cycles or times that the Tool was used on the production unit
    UsageCycles: int = 0
    
    # If components were installed during the operation, this property provides
    # a detailed listing of the components that were installed.
    InstalledComponents: List[InstalledComponent] = field(default_factory=list)