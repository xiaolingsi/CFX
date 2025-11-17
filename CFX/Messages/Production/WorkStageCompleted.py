import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.WorkResult import WorkResult
from CFX.Messages.Structures.PerformanceImpact import PerformanceImpact


@dataclass_json
@dataclass
class WorkStageCompleted(CFXMessage):
    TransactionID: uuid.UUID
    Stage: Stage
    Result: WorkResult
    PerformanceImpacts: List[PerformanceImpact]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, stage: Stage = None, result: WorkResult = None, 
                 performance_impacts: List[PerformanceImpact] = None):
        super().__init__()
        self.type = "CFX.Production.WorkStageCompleted,CFX"
        self.message_name = "CFX.Production.WorkStageCompleted"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.Stage = stage
        self.Result = result or WorkResult.Completed
        self.PerformanceImpacts = performance_impacts or []