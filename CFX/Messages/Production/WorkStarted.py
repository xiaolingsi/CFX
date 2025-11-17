import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition


@dataclass_json
@dataclass
class WorkStarted(CFXMessage):
    PrimaryIdentifier: str
    HermesIdentifier: str
    TransactionID: uuid.UUID
    Lane: int
    UnitCount: int
    Units: List[UnitPosition]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, primary_identifier: str = "", hermes_identifier: str = "", lane: int = None, units: List[UnitPosition] = None,transaction_id: uuid.UUID = None):
        super().__init__()
        self.type = "CFX.Production.WorkStarted,CFX"
        self.message_name = "CFX.Production.WorkStarted"
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.TransactionID = transaction_id or  uuid.uuid4()
        self.Lane = lane
        self.UnitCount = len(units) if units else 0
        self.Units = units or []