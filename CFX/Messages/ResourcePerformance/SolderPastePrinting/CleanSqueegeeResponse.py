from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class CleanSqueegeeResponse(CFXMessage):
    """
    Response to a request from an external source for a squeegee clean
    operation to be performed.
    """
    result: RequestResult = field(default_factory=RequestResult)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.SolderPastePrinting.CleanSqueegeeResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.SolderPastePrinting.CleanSqueegeeResponse"
        self.result = result if result is not None else RequestResult()