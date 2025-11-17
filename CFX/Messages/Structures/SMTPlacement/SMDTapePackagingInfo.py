"""
** NOTE: ADDED in CFX 1.5 **
Describes the packaging infos of an SMD tape
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..PackagingInfo import PackagingInfo


@dataclass_json
@dataclass
class SMDTapePackagingInfo(PackagingInfo):
    """
    ** NOTE: ADDED in CFX 1.5 **
    Describes the packaging infos of an SMD tape
    """
    
    # The width of the tape (in millimeters)
    TapeWidth: float = 0.0
    
    # The pitch (spacing between parts) of the tape (in millimeters)
    TapePitch: float = 0.0
    
    # The diameter of the tape (in millimeters)
    TapeDiameter: float = 0.0
    
    # The thickness of the tape (in millimeters)
    TapeThickness: float = 0.0