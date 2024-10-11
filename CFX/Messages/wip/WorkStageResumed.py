import uuid

from CFX.CFXMessage import CFXMessage
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.StageType import StageType
from CFX.Messages.Structures.Stage import Stage


@dataclass_json
@dataclass
class WorkStageResumed(CFXMessage):
    def to_cfx_json(self):
        return self.to_json()

    TransactionID: uuid.uuid4()
    Stage: Stage

    def __init__(self,stage,transctionID=uuid.uuid4()):
        super().__init__()
        self.type = "CFX.Production.WorkStageResumed,CFX"
        self.message_name = "CFX.Production.WorkStageResumed"
        self.Stage = stage
        self.TransactionID = transctionID


