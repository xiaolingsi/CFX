"""
Describes details of a particular Endpoint that is participating in a CFX network,
and more specifically, is an SMT placement machine. This is a dynamic structure.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from ..Endpoint import Endpoint
from ..DimensionalConstraints import DimensionalConstraints
from .SMTLaneInformation import SMTLaneInformation
from .SMTHeadInformation import SMTHeadInformation
from .SMTPlacementConstraints import SMTPlacementConstraints


@dataclass_json
@dataclass
class SMTPlacementEndpoint(Endpoint):
    """
    Describes details of a particular Endpoint that is participating in a CFX network,
    and more specifically, is an SMT placement machine. This is a dynamic structure.
    """
    
    # The nominal number of components that this endpoint can place per hour.
    NominalPlacementCPH: float = 0.0
    
    # The average (nominal) number of production units per hour this endpoint
    # is capable of producing.
    NominalUnitsPerHour: float = 0.0
    
    # InformationSystem about the production lanes of this SMT placement machine.
    Lanes: List[SMTLaneInformation] = field(default_factory=list)
    
    # InformationSystem about the heads of this SMT placement machine.
    Heads: List[SMTHeadInformation] = field(default_factory=list)
    
    # The placement constraints / capabilities of this endpoint.
    PlacementConstraints: SMTPlacementConstraints = field(default_factory=SMTPlacementConstraints)