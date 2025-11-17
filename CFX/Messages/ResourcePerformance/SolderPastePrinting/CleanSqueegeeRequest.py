from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.SolderPastePrinting import SMTSqueegeeCleanType


@dataclass_json
@dataclass
class CleanSqueegeeRequest(CFXMessage):
    """
    Allows an external source to direct a request to a stencil printer
    to perform a squeegee clean operation.
    """
    clean_type_requested: SMTSqueegeeCleanType = field(default_factory=lambda: SMTSqueegeeCleanType.Normal)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, clean_type_requested=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.SolderPastePrinting.CleanSqueegeeRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.SolderPastePrinting.CleanSqueegeeRequest"
        self.clean_type_requested = clean_type_requested if clean_type_requested is not None else SMTSqueegeeCleanType.Normal