"""
Describes the results of a measurement that was made on a solder paste deposition.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from ..Measurement import Measurement
from ..Image import Image


@dataclass_json
@dataclass
class SolderPasteMeasurement(Measurement):
    """
    Describes the results of a measurement that was made on a solder paste deposition.
    """
    
    # The x dimension (length) of the paste deposition, expressed in millimeters (mm).
    X: float = 0.0
    
    # The expected or nominal x dimension (length) required for this paste deposition, expressed in millimeters (mm).
    EX: float = 0.0
    
    # The x dimension (length) of the paste deposition, expressed in millimeters (mm).
    Y: float = 0.0
    
    # The expected or nominal x dimension (length) required for this paste deposition, expressed in millimeters (mm).
    EY: float = 0.0
    
    # The height of the paste deposition, expressed in millimeters (mm).
    Z: float = 0.0
    
    # The expected or nominal height required for this paste deposition, expressed in millimeters (mm).
    EZ: float = 0.0
    
    # The x location of the center of the paste deposition relative to the center of the pad.
    DX: float = 0.0
    
    # The y location of the center of the paste deposition relative to the center of the pad.
    DY: float = 0.0
    
    # The volume of the paste deposition, expressed in milliliters (ml)
    Vol: float = 0.0
    
    # The expected or nominal volume of the paste deposition, expressed in milliliters (ml)
    EVol: float = 0.0
    
    # An optional image of the deposit formatted in an acceptable MIME image format (JPG, PNG, etc.)
    Image: Optional[Image] = None
    
    # ** NOTE: ADDED in CFX 1.3 **
    # The area of the paste deposition, expressed in square millimeters 
    A: float = 0.0
    
    # ** NOTE: ADDED in CFX 1.3 **
    # The expected area of the paste deposition, expressed in square millimeters 
    EA: float = 0.0
    
    # ** NOTE: ADDED in CFX 1.3 **
    # The position X value in millimeters (mm).
    PX: float = 0.0
    
    # ** NOTE: ADDED in CFX 1.3 **
    # The position Y value in millimeters (mm).
    PY: float = 0.0
    
    # Rotation related information
    # This information is optional, if not available the angles are supposed to be zero
    # ** NOTE: ADDED in CFX 1.3 **
    # The counter-clockwise rotational offset on the X-Y plane (in degrees)
    RXY: Optional[float] = None
    
    # ** NOTE: ADDED in CFX 1.3 **
    # Area Ratio of the related Aperture (Area/WallArea)
    AR: float = 0.0