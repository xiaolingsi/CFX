from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .GeometricObject import GeometricObject

@dataclass_json
@dataclass
class Fiducial(GeometricObject):
    """Fiducial mark for justification (position and orientation) of panels/boards."""
    
    # Type of the fiducial, like "Circle" or "Rect".
    Type: Optional[str] = None