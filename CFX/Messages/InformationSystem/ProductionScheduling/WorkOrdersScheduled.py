from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ScheduledWorkOrder import ScheduledWorkOrder


@dataclass_json
@dataclass
class WorkOrdersScheduled(CFXMessage):
    ScheduledWorkOrders: List[ScheduledWorkOrder]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, scheduled_work_orders: List[ScheduledWorkOrder] = None):
        super().__init__()
        self.type = "CFX.InformationSystem.ProductionScheduling.WorkOrdersScheduled,CFX"
        self.message_name = "CFX.InformationSystem.ProductionScheduling.WorkOrdersScheduled"
        self.ScheduledWorkOrders = scheduled_work_orders or []