from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class GetActiveRecipeRequest(CFXMessage):
    Lane: int
    Stage: Stage

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, stage: Stage, lane: int = 0):
        super().__init__()
        self.type = "CFX.Production.GetActiveRecipeRequest,CFX"
        self.message_name = "CFX.Production.GetActiveRecipeRequest"
        self.Stage = stage
        self.Lane = lane
