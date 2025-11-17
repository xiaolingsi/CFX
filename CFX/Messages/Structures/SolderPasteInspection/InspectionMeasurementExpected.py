"""
** NOTE: ADDED in CFX 1.3 **
A class to represent the expected measurement results of an inspection process. 
This information is tranferred within the Recipe.
Typical example: solder paste inspection (SPI) expected values for the different dimensions
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from ..Measurement import Measurement
from ..Segment import Segment


@dataclass_json
@dataclass
class InspectionMeasurementExpected(Measurement):
    """
    ** NOTE: ADDED in CFX 1.3 **
    A class to represent the expected measurement results of an inspection process. 
    This information is tranferred within the Recipe.
    Typical example: solder paste inspection (SPI) expected values for the different dimensions
    """
    
    # The expected or nominal dimension (length) of the inspection object, expressed in millimeters (mm).
    EX: float = 0.0
    
    # The expected or nominal dimension (length) of the inspection object, expressed in millimeters (mm).
    EY: float = 0.0
    
    # The expected or nominal height of the inspection object, expressed in millimeters (mm).
    # This value conforms to the stencil thickness on the position where the aperture is located
    EZ: float = 0.0
    
    # The expected or nominal X position of the inspection object, expressed in millimeters (mm).
    PX: float = 0.0
    
    # The expected or nominal Y position of the inspection object, expressed in millimeters (mm).
    PY: float = 0.0
    
    # The expected area of the inspection object, expressed in square millimeters 
    EA: float = 0.0
    
    # The expected or nominal volume of the inspection object, expressed in milliliters (ml)
    EVol: float = 0.0
    
    # Area Ratio of the related Aperture (Area/WallArea)
    AR: float = 0.0
    
    # Rotation related information
    # The counter-clockwise rotational offset on the X-Y plane (in degrees)
    # This information is optional, if not available the angles are supposed to be zero
    RXY: Optional[float] = None
    
    # Optional: List of vertices in case of a polygon shape (segments in CFX terms)
    Vertices: List[Segment] = field(default_factory=list)