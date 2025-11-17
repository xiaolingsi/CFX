import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition
from CFX.Messages.Structures.WorkResult import WorkResult
from CFX.Messages.Structures.PerformanceImpact import PerformanceImpact


@dataclass_json
@dataclass
class WorkCompleted(CFXMessage):
    TransactionID: uuid.UUID
    Result: WorkResult
    PrimaryIdentifier: str
    HermesIdentifier: str
    UnitCount: int
    Units: List[UnitPosition]
    PerformanceImpacts: List[PerformanceImpact]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, result: WorkResult = None, primary_identifier: str = "", 
                 hermes_identifier: str = "", units: List[UnitPosition] = None, performance_impacts: List[PerformanceImpact] = None):
        super().__init__()
        self.type = "CFX.Production.WorkCompleted,CFX"
        self.message_name = "CFX.Production.WorkCompleted"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.Result = result or WorkResult.Completed
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.UnitCount = len(units) if units else 0
        self.Units = units or []
        self.PerformanceImpacts = performance_impacts or []