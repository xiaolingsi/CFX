from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class FiducialInfo(object):
    """
    This structure represents a Fiducial element. It is used to enrich the Unit information
    """
    
    FiducialX: float = 0.0
    FiducialY: float = 0.0
    FiducialRXY: float = 0.0
    UniqueIdentifier: Optional[str] = None