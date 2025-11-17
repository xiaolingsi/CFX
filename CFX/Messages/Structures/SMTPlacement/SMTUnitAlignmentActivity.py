"""
A specialized type of Activity that occurs when a unit is aligned (located / positioned) within a stage
of an SMT machine prior to the commencement of work.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from ..UnitAlignmentActivity import UnitAlignmentActivity
from .SMTHeadInformation import SMTHeadInformation


@dataclass_json
@dataclass
class SMTUnitAlignmentActivity(UnitAlignmentActivity):
    """
    A specialized type of Activity that occurs when a unit is aligned (located / positioned) within a stage
    of an SMT machine prior to the commencement of work.
    """
    
    # The Head used for the alignment
    Head: Optional[SMTHeadInformation] = None