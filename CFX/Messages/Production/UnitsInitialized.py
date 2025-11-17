import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier


@dataclass_json
@dataclass
class UnitsInitialized(CFXMessage):
    TransactionID: uuid.UUID
    PrimaryIdentifier: str
    HermesIdentifier: str
    WorkOrderIdentifier: WorkOrderIdentifier
    Units: List[UnitPosition]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, primary_identifier: str = "", hermes_identifier: str = "", 
                 work_order_identifier: WorkOrderIdentifier = None, units: List[UnitPosition] = None):
        super().__init__()
        self.type = "CFX.Production.UnitsInitialized,CFX"
        self.message_name = "CFX.Production.UnitsInitialized"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.WorkOrderIdentifier = work_order_identifier
        self.Units = units or []