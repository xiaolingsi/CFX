"""
Message sent upon completion of the selective soldering process
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from .ZoneData import ZoneData


@dataclass_json
@dataclass
class SelectiveSolderedPCB:
    """
    Message sent upon completion of the selective soldering process
    """
    
    # Unique ID of Production Unit, Panel, or Carrier
    UnitIdentifier: Optional[str] = None
    
    # Logical reference of production unit as defined by CFX position rule (see CFX standard).
    # unit's true unique identifier.  
    UnitPositionNumber: Optional[int] = None
    
    # Data sepcific to a single zone with the
    # Selective Soldering System
    ZoneData: List[ZoneData] = None

    def __init__(self):
        self.ZoneData = []