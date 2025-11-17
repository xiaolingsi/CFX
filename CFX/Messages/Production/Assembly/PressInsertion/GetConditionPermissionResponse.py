import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.PressInsertion.ConditionStep import ConditionStep


@dataclass_json
@dataclass
class GetConditionPermissionResponse(CFXMessage):
    TransactionID: str
    ConditionStep: ConditionStep
    Result: RequestResult

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", condition_step: ConditionStep = None, result: RequestResult = None):
        super().__init__()
        self.type = "CFX.Production.Assembly.PressInsertion.GetConditionPermissionResponse,CFX"
        self.message_name = "CFX.Production.Assembly.PressInsertion.GetConditionPermissionResponse"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.ConditionStep = condition_step
        self.Result = result or RequestResult()