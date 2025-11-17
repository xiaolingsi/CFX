from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class CleanStencilResponse(CFXMessage):
    """
    A response to a request by a remote party for a stencil printer to perform a
    stencil clean operation.
    """
    result: RequestResult = field(default_factory=RequestResult)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.SolderPastePrinting.CleanStencilResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.SolderPastePrinting.CleanStencilResponse"
        self.result = result if result is not None else RequestResult()