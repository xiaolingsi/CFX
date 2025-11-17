from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.RecipeIdentifier import RecipeIdentifier


@dataclass_json
@dataclass
class GetAvailableRecipesResponse(CFXMessage):
    Result: RequestResult
    ActualCount: int
    RecipeCount: int
    Recipes: List[RecipeIdentifier]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, actual_count: int = 0, recipes: List[RecipeIdentifier] = None):
        super().__init__()
        self.type = "CFX.Production.GetAvailableRecipesResponse,CFX"
        self.message_name = "CFX.Production.GetAvailableRecipesResponse"
        self.Result = result or RequestResult()
        self.ActualCount = actual_count
        self.RecipeCount = len(recipes) if recipes else 0
        self.Recipes = recipes or []