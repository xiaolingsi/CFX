import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.RepairedUnit import RepairedUnit


@dataclass_json
@dataclass
class UnitsRepaired(CFXMessage):
    TransactionId: str
    RepairOperator: Operator
    RepairedUnits: List[RepairedUnit]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", repair_operator: Operator = None, repaired_units: List[RepairedUnit] = None):
        super().__init__()
        self.type = "CFX.Production.ReworkAndRepair.UnitsRepaired,CFX"
        self.message_name = "CFX.Production.ReworkAndRepair.UnitsRepaired"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.RepairOperator = repair_operator or Operator()
        self.RepairedUnits = repaired_units or []