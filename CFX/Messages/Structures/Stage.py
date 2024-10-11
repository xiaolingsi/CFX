from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.genericUnits.StageType import StageType


@dataclass_json
@dataclass
class Stage(object):
    StageSequence: int
    StageName: str
    StageType: StageType

    def __init__(self,stageSequence=0,stageName="",stageType = StageType.Work):
        self.StageSequence = stageSequence
        self.StageName = stageName
        self.StageType = stageType

