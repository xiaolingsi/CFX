from CFX.CFXMessage import CFXMessage
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StatusResult import StatusResult


@dataclass_json
@dataclass
class GetActiveRecipeResponse(CFXMessage):
    ActiveRecipeName:str
    ActiveRecipeRevision:str
    Result: RequestResult

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,result,active_recipe_name:str = "",active_recipe_revision:str = ""):
        super().__init__()
        self.type = "CFX.Production.GetActiveRecipeResponse,CFX"
        self.message_name = "CFX.Production.GetActiveRecipeResponse"
        self.ActiveRecipeName = active_recipe_name
        self.ActiveRecipeRevision = active_recipe_revision
        self.Result = result


