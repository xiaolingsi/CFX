from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class UpdateRecipeResponse(CFXMessage):
    Result: RequestResult

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None):
        super().__init__()
        self.type = "CFX.Production.UpdateRecipeResponse,CFX"
        self.message_name = "CFX.Production.UpdateRecipeResponse"
        self.Result = result or RequestResult()