from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Stage import Stage as s

from CFX.CFXMessage import CFXMessage
from CFX.Messages.genericUnits.StageType import StageType


@dataclass_json
@dataclass
class RecipeActivated(CFXMessage):
    RecipeName: str
    Revision: str
    Stage: s

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,stage, recipe_name: str = "", revision: str = ""):
        super().__init__()
        self.type = "CFX.Production.RecipeActivated,CFX"
        self.message_name = "CFX.Production.RecipeActivated"
        self.RecipeName = recipe_name
        self.Revision = revision
        self.Stage = stage


if __name__ == '__main__':
    stage = s(stageType=StageType.Buffer)
    recipeActivated = RecipeActivated(stage=stage, recipe_name="recipe", revision="-1000")
    print(recipeActivated.to_cfx_json())
