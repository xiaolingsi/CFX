from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage


@dataclass_json
@dataclass
class SetupRequirementsChanged(CFXMessage):
    Lane: int
    Stage: Stage

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, lane: int = None, stage: Stage = None):
        super().__init__()
        self.type = "CFX.Production.SetupRequirementsChanged,CFX"
        self.message_name = "CFX.Production.SetupRequirementsChanged"
        self.Lane = lane
        self.Stage = stage