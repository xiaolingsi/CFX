import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.StatusResult import StatusResult


@dataclass_json
@dataclass
class ConditionCompleted(CFXMessage):
    TransactionID: str
    ResultOfCondition: StatusResult

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", result_of_condition: StatusResult = None):
        super().__init__()
        self.type = "CFX.Production.Assembly.PressInsertion.ConditionCompleted,CFX"
        self.message_name = "CFX.Production.Assembly.PressInsertion.ConditionCompleted"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.ResultOfCondition = result_of_condition or StatusResult.Success

