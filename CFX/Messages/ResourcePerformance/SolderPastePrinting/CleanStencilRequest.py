from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.SolderPastePrinting import SMTStencilCleanMode


@dataclass_json
@dataclass
class CleanStencilRequest(CFXMessage):
    """
    Allows an external source to direct a request to a stencil printer
    to perform a stencil clean operation.
    """
    clean_type_requested: SMTStencilCleanMode = field(default_factory=lambda: SMTStencilCleanMode.W)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, clean_type_requested=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.SolderPastePrinting.CleanStencilRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.SolderPastePrinting.CleanStencilRequest"
        self.clean_type_requested = clean_type_requested if clean_type_requested is not None else SMTStencilCleanMode.W
