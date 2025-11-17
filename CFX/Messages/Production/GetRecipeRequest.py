from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class GetRecipeRequest(CFXMessage):
    RecipeName: str
    Revision: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, recipe_name: str = "", revision: str = ""):
        super().__init__()
        self.type = "CFX.Production.GetRecipeRequest,CFX"
        self.message_name = "CFX.Production.GetRecipeRequest"
        self.RecipeName = recipe_name
        self.Revision = revision