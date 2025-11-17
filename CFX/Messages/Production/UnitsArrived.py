from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition


@dataclass_json
@dataclass
class UnitsArrived(CFXMessage):
    PrimaryIdentifier: str
    HermesIdentifier: str
    UnitCount: int
    Units: List[UnitPosition]
    Lane: int

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, primary_identifier: str = "", hermes_identifier: str = "", units: List[UnitPosition] = None, lane: int = None):
        super().__init__()
        self.type = "CFX.Production.UnitsArrived,CFX"
        self.message_name = "CFX.Production.UnitsArrived"
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.UnitCount = len(units) if units else 0
        self.Units = units or []
        self.Lane = lane