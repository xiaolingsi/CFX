import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.WorkStagePauseReason import WorkStagePauseReason


@dataclass_json
@dataclass
class WorkStagePaused(CFXMessage):
    TransactionID: uuid.UUID
    Stage: Stage
    PauseReason: WorkStagePauseReason

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, stage: Stage = None, pause_reason: WorkStagePauseReason = None):
        super().__init__()
        self.type = "CFX.Production.WorkStagePaused,CFX"
        self.message_name = "CFX.Production.WorkStagePaused"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.Stage = stage
        self.PauseReason = pause_reason or WorkStagePauseReason.Unknown
