from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier
from CFX.Messages.Structures.WorkOrderStatus import WorkOrderStatus


@dataclass_json
@dataclass
class WorkOrderStatusUpdated(CFXMessage):
    WorkOrderIdentifier: WorkOrderIdentifier
    NewStatus: WorkOrderStatus
    PreviousStatus: WorkOrderStatus

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, work_order_identifier: WorkOrderIdentifier = None, 
                 new_status: WorkOrderStatus = None, previous_status: WorkOrderStatus = None):
        super().__init__()
        self.type = "CFX.InformationSystem.WorkOrderManagement.WorkOrderStatusUpdated,CFX"
        self.message_name = "CFX.InformationSystem.WorkOrderManagement.WorkOrderStatusUpdated"
        self.WorkOrderIdentifier = work_order_identifier
        self.NewStatus = new_status
        self.PreviousStatus = previous_status