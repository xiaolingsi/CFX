from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage


@dataclass_json
@dataclass
class ActivateRecipeRequest(CFXMessage):
    RecipeName: str
    Revision: str
    Lane: int
    Stage: Stage

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, recipe_name: str = "", revision: str = "", lane: int = None, stage: Stage = None):
        super().__init__()
        self.type = "CFX.Production.ActivateRecipeRequest,CFX"
        self.message_name = "CFX.Production.ActivateRecipeRequest"
        self.RecipeName = recipe_name
        self.Revision = revision
        self.Lane = lane
        self.Stage = stage