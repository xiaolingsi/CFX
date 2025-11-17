from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier


@dataclass_json
@dataclass
class RecipeDeactivated(CFXMessage):
    RecipeName: str
    Revision: str
    Lane: int
    Stage: Stage
    WorkOrderIdentifier: WorkOrderIdentifier

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, recipe_name: str = "", revision: str = "", lane: int = None, stage: Stage = None, 
                 work_order_identifier: WorkOrderIdentifier = None):
        super().__init__()
        self.type = "CFX.Production.RecipeDeactivated,CFX"
        self.message_name = "CFX.Production.RecipeDeactivated"
        self.RecipeName = recipe_name
        self.Revision = revision
        self.Lane = lane
        self.Stage = stage
        self.WorkOrderIdentifier = work_order_identifier