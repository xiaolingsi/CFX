from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.Recipe import Recipe


@dataclass_json
@dataclass
class GetRecipeResponse(CFXMessage):
    Result: RequestResult
    Recipe: Recipe

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, recipe: Recipe = None):
        super().__init__()
        self.type = "CFX.Production.GetRecipeResponse,CFX"
        self.message_name = "CFX.Production.GetRecipeResponse"
        self.Result = result or RequestResult()
        self.Recipe = recipe or Recipe()