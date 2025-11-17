from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class UnlockStationRequest(CFXMessage):
    Lane: int
    Stage: Stage
    Requestor: Operator

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, lane: int = None, stage: Stage = None, requestor: Operator = None):
        super().__init__()
        self.type = "CFX.Production.UnlockStationRequest,CFX"
        self.message_name = "CFX.Production.UnlockStationRequest"
        self.Lane = lane
        self.Stage = stage
        self.Requestor = requestor