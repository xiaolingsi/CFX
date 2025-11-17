from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Recipe import Recipe
from CFX.Messages.Structures.RecipeModificationReason import RecipeModificationReason


@dataclass_json
@dataclass
class UpdateRecipeRequest(CFXMessage):
    Overwrite: bool
    Recipe: Recipe
    Reason: RecipeModificationReason

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, recipe: Recipe = None, overwrite: bool = False, reason: RecipeModificationReason = None):
        super().__init__()
        self.type = "CFX.Production.UpdateRecipeRequest,CFX"
        self.message_name = "CFX.Production.UpdateRecipeRequest"
        self.Overwrite = overwrite
        self.Recipe = recipe
        self.Reason = reason or RecipeModificationReason.Unspecified