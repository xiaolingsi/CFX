from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .PerformanceImpactCause import PerformanceImpactCause

@dataclass_json
@dataclass
class PerformanceImpact:
    """** NOTE: ADDED in CFX 1.6 **
    Performance impacts of a machine (i.e., in case of lower-than-expected performance)
    It shall be "null" or not sent at all if the machine doesn't support the PerformanceImpact attribute.
    An empty list indicates that the machine is running at "best-performance"""
    
    # The cause of this performance impact.
    Cause: Optional[PerformanceImpactCause] = None