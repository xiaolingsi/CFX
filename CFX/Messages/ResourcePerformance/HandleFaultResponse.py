from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class HandleFaultResponse(CFXMessage):
    Result: RequestResult = field(default_factory=RequestResult)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.HandleFaultResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.HandleFaultResponse"
        self.Result = result if result is not None else RequestResult()



