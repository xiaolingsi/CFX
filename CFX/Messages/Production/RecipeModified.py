from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.RecipeModificationReason import RecipeModificationReason
from CFX.Messages.UnitPojo.Stage import Stage as s
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier
from CFX.CFXMessage import CFXMessage
from CFX.Messages.genericUnits.StageType import StageType


@dataclass_json
@dataclass
class RecipeModified(CFXMessage):
    RecipeName: str
    Revision: str
    ModifiedBy: Operator
    Notes: str
    Reason: RecipeModificationReason
    WorkOrderIdentifier: WorkOrderIdentifier

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, recipe_name: str = "", revision: str = "",modified_by :Operator = None,
                 reason:RecipeModificationReason = RecipeModificationReason.Unspecified,
                 workOrderIdentifier:WorkOrderIdentifier = None,notes:str = ""):
        super().__init__()
        self.type = "CFX.Production.RecipeModified,CFX"
        self.message_name = "CFX.Production.RecipeModified"
        self.RecipeName = recipe_name
        self.Revision = revision
        self.ModifiedBy = modified_by
        self.Notes = notes
        self.Reason = reason
        self.WorkOrderIdentifier = workOrderIdentifier


if __name__ == '__main__':
    recipeModified = RecipeModified(recipe_name="recipe", revision="-1000")
    print(recipeModified.to_cfx_json())
