"""
** NOTE: ADDED in CFX 1.3 **
Represents generic sub-resources of a generic head. For example, camera
mounted on head in a specific position
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from ..ResourceInformation import ResourceInformation
from ..Camera import Camera
from ..RotationAxis import RotationAxis


@dataclass_json
@dataclass
class SMTHeadResource(ResourceInformation):
    """
    ** NOTE: ADDED in CFX 1.3 **
    Represents generic sub-resources of a generic head. For example, camera
    mounted on head in a specific position
    """
    
    # A list of camera located on the Head
    Cameras: List[Camera] = field(default_factory=list)
    
    # If applicable, rotation axis of part located on Head
    RotationAxes: List[RotationAxis] = field(default_factory=list)