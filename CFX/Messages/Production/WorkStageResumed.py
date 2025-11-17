import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage


@dataclass_json
@dataclass
class WorkStageResumed(CFXMessage):
    TransactionID: uuid.UUID
    Stage: Stage

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, stage: Stage = None):
        super().__init__()
        self.type = "CFX.Production.WorkStageResumed,CFX"
        self.message_name = "CFX.Production.WorkStageResumed"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.Stage = stage