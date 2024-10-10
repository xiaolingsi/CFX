import uuid

from CFX.CFXMessage import CFXMessage
from CFX.Messages.UnitPojo.UnitPosition import UnitPosition
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.StageType import StageType
from CFX.Messages.UnitPojo.Stage import Stage
from CFX.Messages.genericUnits.WorkStagePauseReason import WorkStagePauseReason


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


if __name__ == '__main__':
    workStageResumed = WorkStageResumed(stage=Stage(stageName="StageNameBB",stageType=StageType.Work))
    print(workStageResumed.to_cfx_json())