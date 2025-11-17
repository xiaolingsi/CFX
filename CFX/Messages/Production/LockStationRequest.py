from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.LockReason import LockReason


@dataclass_json
@dataclass
class LockStationRequest(CFXMessage):
    Lane: int
    Stage: Stage
    Reason: LockReason
    Requestor: Operator

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, lane: int = 0, stage: Stage = None, reason: LockReason = None, requestor: Operator = None):
        super().__init__()
        self.type = "CFX.Production.LockStationRequest,CFX"
        self.message_name = "CFX.Production.LockStationRequest"
        self.Lane = lane
        self.Stage = stage
        self.Reason = reason or LockReason.GeneralLock
        self.Requestor = requestor