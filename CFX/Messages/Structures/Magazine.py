from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from .HermesUnit import HermesUnit

@dataclass_json
@dataclass
class Magazine:
    """** NOTE: ADDED in CFX 1.3 **
    Structure that contains information related to a magazine."""
    
    def __post_init__(self):
        if self.HermesUnits is None:
            self.HermesUnits = []
    
    # Barcode of a magazine, required to identify the magazine.
    MagazineId: Optional[str] = None
    
    # List of Hermes units (i.e. Boards) contained in the magazine.
    HermesUnits: List[HermesUnit] = field(default_factory=list)