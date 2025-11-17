from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class OperatorActivated(CFXMessage):
    Operator: Operator

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, operator: Operator = None):
        super().__init__()
        self.type = "CFX.Production.OperatorActivated,CFX"
        self.message_name = "CFX.Production.OperatorActivated"
        self.Operator = operator