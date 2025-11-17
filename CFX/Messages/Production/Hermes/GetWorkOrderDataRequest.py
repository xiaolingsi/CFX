from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier


@dataclass_json
@dataclass
class GetWorkOrderDataRequest(CFXMessage):
    WorkOrderIdentifier: WorkOrderIdentifier
    UnitIdentifier: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, work_order_identifier: WorkOrderIdentifier = None, unit_identifier: str = ""):
        super().__init__()
        self.type = "CFX.Production.Hermes.GetWorkOrderDataRequest,CFX"
        self.message_name = "CFX.Production.Hermes.GetWorkOrderDataRequest"
        self.WorkOrderIdentifier = work_order_identifier or WorkOrderIdentifier()
        self.UnitIdentifier = unit_identifier