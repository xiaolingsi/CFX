from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json
from .UnitPosition import UnitPosition
from .FiducialInfo import FiducialInfo


@dataclass_json
@dataclass
class UnitInfo(UnitPosition):
    """
    ** NOTE: ADDED in CFX 1.4 **
    This structure contains detailed information (e.g., BadMarks, Fiducials) about a one of a set of production units that are processed simultaneously under a single transaction by an endpoint.
    Units may be identified in one of two ways:
        1.  The UnitIdentifier property represents the actual unique identifier of the production unit.
        2.  The UnitIdentifier property represents the unique identifier of the "carrier" or "PCB panel"
            AND the PositionNumber property represents the position of the unit within the carrier/panel.
            PositionNumber's are established as defined in the CFX Standard.
    {
        "UnitIdentifier": "CARRIER5566",
        "PositionNumber": 1,
        "PositionName": "CIRCUIT1",
        "X": 0.254,
        "Y": 0.556,
        "Rotation": 0.0,
        "FlipX": false,
        "FlipY": false,
        "BadMark": 0,
        "FiducialCount": 2,
        "Fiducials": [
        {
          "FiducialX": "10.2",
          "FiducialY": 1.3,
          "FiducialRXY": "0.5"
        },
        {
          "FiducialX": "20.8",
          "FiducialY": 7.3,
          "FiducialRXY": "0.0"
        }
      ],
       "CRDs" : []
    }
    """
    
    # Is Unit good or not good for production or unknown:
    # 0: unknown whether unit is good or not good for production
    # 1: unit is good for production
    # 2: unit is not good for production
    BadMark: Optional[int] = None
    
    # The number of Fiducials
    FiducialCount: Optional[int] = None
    
    # An optional list of structures with Fiducial coordinates and rotational offset
    Fiducials: List[FiducialInfo] = field(default_factory=list)
    
    # ** NOTE: ADDED in CFX 1.7 **
    # An optional list of component designators (instances of a part) on a production unit(s) to be associated with this measurement.
    # May include sub-components in "." notation.  Examples:  R1, R2, R3 or  R2.3 (R2, pin 3)
    CRDs: List[str] = field(default_factory=list)