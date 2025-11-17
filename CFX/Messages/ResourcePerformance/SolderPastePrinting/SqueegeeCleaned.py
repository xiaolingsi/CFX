from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.SolderPastePrinting import SMTSqueegee, SMTSqueegeeCleanType


@dataclass_json
@dataclass
class SqueegeeCleaned(CFXMessage):
    """
    Indicates that a squeegee clean operation has been performed.
    """
    squeegee: Optional[SMTSqueegee] = None
    squeegee_clean_type: SMTSqueegeeCleanType = field(default_factory=lambda: SMTSqueegeeCleanType.Normal)
    time_since_last_clean: Optional[str] = None
    cycles_since_last_clean: int = 0
    squeegee_clean_cycles: int = 0
    squeegee_clean_time: Optional[str] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, squeegee=None, squeegee_clean_type=None, time_since_last_clean=None, 
                 cycles_since_last_clean=0, squeegee_clean_cycles=0, squeegee_clean_time=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.SolderPastePrinting.SqueegeeCleaned,CFX"
        self.message_name = "CFX.ResourcePerformance.SolderPastePrinting.SqueegeeCleaned"
        self.squeegee = squeegee
        self.squeegee_clean_type = squeegee_clean_type if squeegee_clean_type is not None else SMTSqueegeeCleanType.Normal
        self.time_since_last_clean = time_since_last_clean
        self.cycles_since_last_clean = cycles_since_last_clean
        self.squeegee_clean_cycles = squeegee_clean_cycles
        self.squeegee_clean_time = squeegee_clean_time