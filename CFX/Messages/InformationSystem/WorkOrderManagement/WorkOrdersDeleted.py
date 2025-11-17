from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier


@dataclass_json
@dataclass
class WorkOrdersDeleted(CFXMessage):
    WorkOrderIdentifiers: List[WorkOrderIdentifier]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, work_order_identifiers: List[WorkOrderIdentifier] = None):
        super().__init__()
        self.type = "CFX.InformationSystem.WorkOrderManagement.WorkOrdersDeleted,CFX"
        self.message_name = "CFX.InformationSystem.WorkOrderManagement.WorkOrdersDeleted"
        self.WorkOrderIdentifiers = work_order_identifiers or []