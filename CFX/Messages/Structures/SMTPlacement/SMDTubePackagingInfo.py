"""
** NOTE: ADDED in CFX 1.5 **
Describes the packaging infos of an SMD tube
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..PackagingInfo import PackagingInfo


@dataclass_json
@dataclass
class SMDTubePackagingInfo(PackagingInfo):
    """
    ** NOTE: ADDED in CFX 1.5 **
    Describes the packaging infos of an SMD tube
    """
    
    # The width of the tube (in millimeters)
    TubeWidth: float = 0.0
    
    # The pitch (spacing between parts) of the tube (in millimeters)
    TubePitch: float = 0.0
    
    # The length of the tube (in millimeters)
    TubeLength: float = 0.0
    
    # The thickness of the tube (in millimeters)
    TubeThickness: float = 0.0