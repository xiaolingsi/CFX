from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .InspectionObject import InspectionObject
from ..Geometry.Vector3 import Vector3

@dataclass_json
@dataclass
class GeometricObject(InspectionObject):
    """The geometry of a component (board, resistor, capacitor, pin, ...)."""
    
    # X=Width, Y=Height, Z=Depth, in mm.
    Size: Optional[Vector3] = None
    
    # The position in global coordinates, i.e. all position shifts and rotations of the
    # parent objects (recursively) are factored in.
    # Given in mm, as right handed coordinates.
    Position: Optional[Vector3] = None
    
    # The global rotation, i.e. all rotations of the parent objects (recursively) factored in.
    # X=RotationAroundXAxis, Y=RotationAroundYAxis, Z=RotationAroundZAxis, in degrees [0..360]
    # around the center of this object, right hand rule.
    # Optional value. If missing in the recipe, then it is assumed to be (0.0, 0.0, 0.0).
    Rotation: Optional[Vector3] = None