from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier


@dataclass_json
@dataclass
class WorkOrderQuantityUpdated(CFXMessage):
    WorkOrderIdentifier: WorkOrderIdentifier
    NewQuantity: float
    PreviousQuantity: float

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, work_order_identifier: WorkOrderIdentifier = None, new_quantity: float = 0.0, 
                 previous_quantity: float = None):
        super().__init__()
        self.type = "CFX.InformationSystem.WorkOrderManagement.WorkOrderQuantityUpdated,CFX"
        self.message_name = "CFX.InformationSystem.WorkOrderManagement.WorkOrderQuantityUpdated"
        self.WorkOrderIdentifier = work_order_identifier
        self.NewQuantity = new_quantity
        self.PreviousQuantity = previous_quantity