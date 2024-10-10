import uuid

from CFX.CFXMessage import CFXMessage
from CFX.Messages.UnitPojo.UnitPosition import UnitPosition
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.StageType import StageType
from CFX.Messages.genericUnits.WorkResult import WorkResult
from CFX.Messages.UnitPojo.Stage import Stage


@dataclass_json
@dataclass
class WorkStageCompleted(CFXMessage):
    def to_cfx_json(self):
        return self.to_json()

    TransactionID: uuid.uuid4()
    Stage: Stage
    Result: WorkResult

    def __init__(self,stage,transctionID=uuid.uuid4(),result:WorkResult = WorkResult.Completed):
        super().__init__()
        self.type = "CFX.Production.WorkStageCompleted,CFX"
        self.message_name = "CFX.Production.WorkStageCompleted"
        self.Stage = stage
        self.TransactionID = transctionID
        self.Result = result


if __name__ == '__main__':
    workStageCompleted = WorkStageCompleted(stage=Stage(stageName="StageName",stageType=StageType.Work),result=WorkResult.Skipped)
    print(workStageCompleted.to_cfx_json())