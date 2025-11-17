"""
Describes a lane for an endpoint that is an SMT placement machine.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional
from ..DimensionalConstraints import DimensionalConstraints


@dataclass_json
@dataclass
class SMTLaneInformation:
    """
    Describes a lane for an endpoint that is an SMT placement machine.
    """
    
    # The lane number. Corresponds with Lane property in production messages.
    LaneNumber: Optional[int] = None
    
    # The friendly name of this lane.
    LaneName: str = ""
    
    # The maximum and minimum dimensions that a PCB panel or fixture must conform
    # to in order to be processed by this lane.
    SupportedPCBDimensions: Optional[DimensionalConstraints] = None