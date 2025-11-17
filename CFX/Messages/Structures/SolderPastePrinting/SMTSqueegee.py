"""
Describes a squeegee that is used in the course of printing solder paste on to a PCB
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..Tool import Tool
from ..Cleaning.CleaningState import CleaningState


@dataclass_json
@dataclass
class SMTSqueegee(Tool):
    """
    Describes a squeegee that is used in the course of printing solder paste on to a PCB
    """
    
    # ** NOTE: ADDED in CFX 1.5 **
    # SMT Squeegee cleaning states
    CleaningState: CleaningState = CleaningState.Unknown