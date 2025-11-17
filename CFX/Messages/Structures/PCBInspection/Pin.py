from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .GeometricObject import GeometricObject

@dataclass_json
@dataclass
class Pin(GeometricObject):
    """The pins of a component (typically two on resistors, many more on ICs)."""
    
    pass