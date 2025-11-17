import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.PressInsertion.ConditionStep import ConditionStep


@dataclass_json
@dataclass
class GetConditionPermissionRequest(CFXMessage):
    TransactionID: str
    ConditionStep: ConditionStep
    Data: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", condition_step: ConditionStep = None, data: str = ""):
        super().__init__()
        self.type = "CFX.Production.Assembly.PressInsertion.GetConditionPermissionRequest,CFX"
        self.message_name = "CFX.Production.Assembly.PressInsertion.GetConditionPermissionRequest"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.ConditionStep = condition_step
        self.Data = data