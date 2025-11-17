import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.PersonalizedUnit import PersonalizedUnit


@dataclass_json
@dataclass
class UnitsPersonalized(CFXMessage):
    TransactionId: str
    PersonalizedUnits: List[PersonalizedUnit]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", personalized_units: List[PersonalizedUnit] = None):
        super().__init__()
        self.type = "CFX.Production.Assembly.UnitsPersonalized,CFX"
        self.message_name = "CFX.Production.Assembly.UnitsPersonalized"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.PersonalizedUnits = personalized_units or []