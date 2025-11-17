from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class Head(object):
    """
    Represents a generic head on an automated endpoint. This is the base class of a dynamic structure, permitting
    for specialized heads derived from this class. Examples of heads are SMT placement heads used in the placement
    of electronic components on PCB's, or a dispensing head, used in the dispensing of fluids or glues.
    """
    
    HeadId: Optional[str] = None
    HeadSequence: int = 1
    HeadName: Optional[str] = None

    def __init__(self, head_id="", head_sequence=1, head_name=""):
        self.HeadId = head_id
        self.HeadSequence = head_sequence
        self.HeadName = head_name