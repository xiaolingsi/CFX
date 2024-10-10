from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.UnitPojo.Stage import Stage


@dataclass_json
@dataclass
class StageInformation(object):
    Stage: Stage

    def __init__(self, stage: Stage):
        self.Stage = stage
