import uuid

from CFX.CFXMessage import CFXMessage
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.StageType import StageType
from CFX.Messages.Structures.Stage import Stage


@dataclass_json
@dataclass
class WorkStageStarted(CFXMessage):
    def to_cfx_json(self):
        return self.to_json()

    TransactionID: uuid.uuid4()
    Stage: Stage

    def __init__(self,stage,transctionID=uuid.uuid4()):
        super().__init__()
        self.type = "CFX.Production.WorkStageStarted,CFX"
        self.message_name = "CFX.Production.WorkStageStarted"
        self.Stage = stage
        self.TransactionID = transctionID


if __name__ == '__main__':
    workStageStarted = WorkStageStarted(stage=Stage(stageName="StageNameCC",stageType=StageType.Work))
    print(workStageStarted.to_cfx_json())