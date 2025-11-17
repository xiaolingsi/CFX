"""
Describes a particular nozzle and head combination that was used in the course of production.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional
from ..Tool import Tool


@dataclass_json
@dataclass
class SMTHeadAndNozzle(Tool):
    """
    Describes a particular nozzle and head combination that was used in the course of production.
    """
    
    # The name or identifier of SMT head associated with this SMT Nozzle.
    HeadId: str = ""
    
    # The spindle number on the head to which this SMT Nozzle is attached
    HeadNozzleNumber: Optional[int] = None
    
    # The type or model name of this SMT Nozzle
    NozzleType: str = ""