from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class NamedObject:
    """An object that can be identified by its name."""
    
    # The name of this object, like "C1", "R1", "Fiducial_1", "Pin1"
    Name: Optional[str] = None