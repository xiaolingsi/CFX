import uuid

from CFX.CFXMessage import CFXMessage
from CFX.Messages.UnitPojo.UnitPosition import UnitPosition
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.StageType import StageType
from CFX.Messages.genericUnits.WorkResult import WorkResult
from CFX.Messages.UnitPojo.Stage import Stage
from CFX.Messages.genericUnits.WorkStagePauseReason import WorkStagePauseReason


@dataclass_json
@dataclass
class WorkStagePaused(CFXMessage):
    def to_cfx_json(self):
        return self.to_json()

    TransactionID: uuid.uuid4()
    Stage: Stage
    PauseReason: WorkStagePauseReason

    def __init__(self,stage,transctionID=uuid.uuid4(),pauseReason:WorkStagePauseReason = WorkStagePauseReason.Unknown):
        super().__init__()
        self.type = "CFX.Production.WorkStagePaused,CFX"
        self.message_name = "CFX.Production.WorkStagePaused"
        self.Stage = stage
        self.TransactionID = transctionID
        self.PauseReason = pauseReason


if __name__ == '__main__':
    workStagePaused = WorkStagePaused(stage=Stage(stageName="StageNameAA",stageType=StageType.Work),pauseReason=WorkStagePauseReason.Unknown)
    print(workStagePaused.to_cfx_json())