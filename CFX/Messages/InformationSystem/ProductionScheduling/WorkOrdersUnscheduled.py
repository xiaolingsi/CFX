from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ScheduledWorkOrderIdentifier import ScheduledWorkOrderIdentifier


@dataclass_json
@dataclass
class WorkOrdersUnscheduled(CFXMessage):
    ScheduledWorkOrderIdentifiers: List[ScheduledWorkOrderIdentifier]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, scheduled_work_order_identifiers: List[ScheduledWorkOrderIdentifier] = None):
        super().__init__()
        self.type = "CFX.InformationSystem.ProductionScheduling.WorkOrdersUnscheduled,CFX"
        self.message_name = "CFX.InformationSystem.ProductionScheduling.WorkOrdersUnscheduled"
        self.ScheduledWorkOrderIdentifiers = scheduled_work_order_identifiers or []