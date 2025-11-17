from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.SolderPastePrinting import SMTStencil, SMTStencilCleanMode


@dataclass_json
@dataclass
class StencilCleaned(CFXMessage):
    """
    Indicates that a stencil clean operation has been performed.
    """
    stencil: Optional[SMTStencil] = None
    stencil_clean_mode: SMTStencilCleanMode = field(default_factory=lambda: SMTStencilCleanMode.D)
    time_since_last_clean: Optional[str] = None
    cycles_since_last_clean: int = 0
    stencil_clean_cycles: int = 0
    stencil_clean_time: Optional[str] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, stencil=None, stencil_clean_mode=None, time_since_last_clean=None, 
                 cycles_since_last_clean=0, stencil_clean_cycles=0, stencil_clean_time=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.SolderPastePrinting.StencilCleaned,CFX"
        self.message_name = "CFX.ResourcePerformance.SolderPastePrinting.StencilCleaned"
        self.stencil = stencil
        self.stencil_clean_mode = stencil_clean_mode if stencil_clean_mode is not None else SMTStencilCleanMode.D
        self.time_since_last_clean = time_since_last_clean
        self.cycles_since_last_clean = cycles_since_last_clean
        self.stencil_clean_cycles = stencil_clean_cycles
        self.stencil_clean_time = stencil_clean_time