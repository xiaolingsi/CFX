"""
A specialized type of fault that is produced by an endpoint that is a reflow oven.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..Fault import Fault
from .ReflowOvenFaultType import ReflowOvenFaultType


@dataclass_json
@dataclass
class ReflowOvenFault(Fault):
    """
    A specialized type of fault that is produced by an endpoint that is a reflow oven.
    """
    
    # The type of this reflow oven fault.
    ReflowOvenFaultType: ReflowOvenFaultType