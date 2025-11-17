import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.Activity import Activity


@dataclass_json
@dataclass
class ActivitiesExecuted(CFXMessage):
    TransactionID: uuid.UUID
    Stage: Stage
    Activities: List[Activity]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, stage: Stage = None, activities: List[Activity] = None):
        super().__init__()
        self.type = "CFX.Production.ActivitiesExecuted,CFX"
        self.message_name = "CFX.Production.ActivitiesExecuted"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.Stage = stage
        self.Activities = activities or []