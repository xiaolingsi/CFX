from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from .Repair import Repair
from .RepairResult import RepairResult

@dataclass_json
@dataclass
class RepairedUnit:
    """** NOTE: ADDED in CFX 1.4 **
    Describes the results of repairs performed on a single production unit."""
    
    def __post_init__(self):
        if self.Repairs is None:
            self.Repairs = []
    
    # Unique ID of Production Unit, Panel, or Carrier
    UnitIdentifier: Optional[str] = None
    
    # Logical reference of production unit as defined by CFX position rule (see CFX standard)
    UnitPositionNumber: Optional[int] = 0
    
    # The overall result of the repairs performed on this unit
    OverallResult: RepairResult = RepairResult.RepairSuccessful
    
    # A list of the Repairs performed, along with the results
    Repairs: List[Repair] = field(default_factory=list)