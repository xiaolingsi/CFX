"""
A specific type of fault that is produced by endpoints responsible
for the picking and placing of SMD components
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from ..Fault import Fault
from ..ComponentDesignator import ComponentDesignator
from ..MaterialLocation import MaterialLocation
from .SMTPlacementFaultType import SMTPlacementFaultType
from .SMTHeadAndNozzle import SMTHeadAndNozzle


@dataclass_json
@dataclass
class SMTPlacementFault(Fault):
    """
    A specific type of fault that is produced by endpoints responsible
    for the picking and placing of SMD components
    """
    
    # The specific type of SMT placement fault
    PlacementFaultType: SMTPlacementFaultType = SMTPlacementFaultType.PickupError
    
    # An integer representing the step in the program/recipe that was
    # being executed when the fault occurred (where applicable)
    ProgramStep: int = 0
    
    # Identifies to specific component the placer was trying to place
    # when the fault occurred (where applicable)
    Designator: ComponentDesignator = field(default_factory=ComponentDesignator)
    
    # The material carrier location related to this fault (where applicable)
    MaterialLocation: MaterialLocation = field(default_factory=MaterialLocation)
    
    # The placement head and nozzle related to this fault (where applicable)
    HeadAndNozzle: SMTHeadAndNozzle = field(default_factory=SMTHeadAndNozzle)