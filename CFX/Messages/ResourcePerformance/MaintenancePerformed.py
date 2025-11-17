from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaintenanceType import MaintenanceType
from CFX.Messages.Structures.ConsumedMaterial import ConsumedMaterial
from CFX.Messages.Structures.MaintenanceTask import MaintenanceTask


@dataclass_json
@dataclass
class MaintenancePerformed(CFXMessage):
    """
    Sent by an endpoint when maintenance has been performed.
    """
    MaintenanceType: MaintenanceType = field(default_factory=lambda: MaintenanceType.Preventive)
    MaintenanceOrderNumber: Optional[str] = None
    MaintenanceJobCode: Optional[str] = None
    ConsumedMaterials: List[ConsumedMaterial] = field(default_factory=list)
    Tasks: List[MaintenanceTask] = field(default_factory=list)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, maintenance_type=None, maintenance_order_number=None, maintenance_job_code=None, 
                 consumed_materials=None, tasks=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.MaintenancePerformed,CFX"
        self.message_name = "CFX.ResourcePerformance.MaintenancePerformed"
        self.MaintenanceType = maintenance_type if maintenance_type is not None else MaintenanceType.Preventive
        self.MaintenanceOrderNumber = maintenance_order_number
        self.MaintenanceJobCode = maintenance_job_code
        self.ConsumedMaterials = consumed_materials if consumed_materials is not None else []
        self.Tasks = tasks if tasks is not None else []
