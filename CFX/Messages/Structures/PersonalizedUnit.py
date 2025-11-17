from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from .Characteristic import Characteristic

@dataclass_json
@dataclass
class PersonalizedUnit:
    """Describes how a particular production unit has been personalized"""
    
    def __post_init__(self):
        if self.Characteristics is None:
            self.Characteristics = []
    
    # Unique ID of Production Unit, Panel, or Carrier
    UnitIdentifier: Optional[str] = None
    
    # Logical reference of production unit as defined by CFX position rule (refer to CFX standard).
    UnitPositionNumber: Optional[int] = None
    
    # A list of personalized characteristics that have been applied to the production unit
    Characteristics: List[Characteristic] = field(default_factory=list)