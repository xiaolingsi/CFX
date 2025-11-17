from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.WorkOrder import WorkOrder


@dataclass_json
@dataclass
class WorkOrdersCreated(CFXMessage):
    NewOrders: List[WorkOrder]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, new_orders: List[WorkOrder] = None):
        super().__init__()
        self.type = "CFX.InformationSystem.WorkOrderManagement.WorkOrdersCreated,CFX"
        self.message_name = "CFX.InformationSystem.WorkOrderManagement.WorkOrdersCreated"
        self.NewOrders = new_orders or []