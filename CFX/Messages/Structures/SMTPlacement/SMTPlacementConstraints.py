"""
Describes the placement constraints / capabilities of an SMT Placement Machine
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class SMTPlacementConstraints:
    """
    Describes the placement constraints / capabilities of an SMT Placement Machine
    """
    
    # The minimum body size in the X dimension that a component
    # must be in order to be placed.
    MinumumComponentBodySizeX: float = 0.0
    
    # The maximum body size in the X dimension that a component
    # may be in order to be placed.
    MaximumComponentBodySizeX: float = 0.0
    
    # The minimum body size in the Y dimension that a component
    # must be in order to be placed.
    MinumumComponentBodySizeY: float = 0.0
    
    # The maximum body size in the Y dimension that a component
    # may be in order to be placed.
    MaximumComponentBodySizeY: float = 0.0
    
    # The minimum height that a component
    # must be in order to be placed.
    MinumumComponentHeight: float = 0.0
    
    # The maximum height that a component
    # may be in order to be placed.
    MaximumComponentHeight: float = 0.0
    
    # The minimum lead width that a component
    # must have in order to be placed.
    MinimumLeadWidth: float = 0.0
    
    # The minimum ball pitch that a BGA type component
    # must have in order to be placed.
    MinimumBGAPitch: float = 0.0
    
    # The minimum lead pitch that an SOIC type component
    # must have in order to be placed.
    MinimumSOICPitch: float = 0.0
    
    # The minimum amount of pressure that will be exerted on components during placement,
    # expressed in kPa
    MinimumMountingPressure: float = 0.0
    
    # The minimum amount of pressure that will be exerted on components during placement,
    # expressed in kPa
    MaximumMountingPressure: float = 0.0