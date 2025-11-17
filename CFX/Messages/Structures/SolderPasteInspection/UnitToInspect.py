"""
** NOTE: ADDED in CFX 1.3 **
Provides recipe information of a given Unit. The units is uniquely identified by the UnitPositionNumber
Rules to generate the UnitPositionNumber are described in the CFX documentation
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from .InspectionItem import InspectionItem


@dataclass_json
@dataclass
class UnitToInspect:
    """
    ** NOTE: ADDED in CFX 1.3 **
    Provides recipe information of a given Unit. The units is uniquely identified by the UnitPositionNumber
    Rules to generate the UnitPositionNumber are described in the CFX documentation
    """
    
    # Logical reference of production unit as defined by CFX position rule (see CFX standard)
    UnitPositionNumber: int = 0
    
    # Optional name of the Unit
    Name: Optional[str] = None
    
    # A list of child object which are to be inspected
    ChildObjects: List[InspectionItem] = field(default_factory=list)