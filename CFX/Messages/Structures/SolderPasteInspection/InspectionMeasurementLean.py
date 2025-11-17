"""
** NOTE: ADDED in CFX 1.3 **
A class to represent the dynamic measurement results of an inspection process without the 
overhead of the static properties which are already tranferred within the Recipe.
The static properties are provide in the CFX.Structures.InspectionMeasurementTarget
Typical example: solder paste inspection (SPI)
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from ..Measurement import Measurement
from ..Image import Image


@dataclass_json
@dataclass
class InspectionMeasurementLean(Measurement):
    """
    ** NOTE: ADDED in CFX 1.3 **
    A class to represent the dynamic measurement results of an inspection process without the 
    overhead of the static properties which are already tranferred within the Recipe.
    The static properties are provide in the CFX.Structures.InspectionMeasurementTarget
    Typical example: solder paste inspection (SPI)
    """
    
    # The x dimension (length) of the inspection object, expressed in millimeters (mm).
    X: float = 0.0
    
    # The x dimension (length) of the inspection object, expressed in millimeters (mm).
    Y: float = 0.0
    
    # The height of the inspection object, expressed in millimeters (mm).
    Z: float = 0.0
    
    # The x location of the center of the inspection object relative to the center of the pad.
    DX: float = 0.0
    
    # The y location of the center of the inspection object relative to the center of the pad.
    DY: float = 0.0
    
    # The volume of the inspection object, expressed in milliliters (ml)
    Vol: float = 0.0
    
    # The area of the inspection object, expressed in square millimeters 
    A: float = 0.0
    
    # An optional image of the deposit formatted in an acceptable MIME image format (JPG, PNG, etc.)
    Image: Optional[Image] = None