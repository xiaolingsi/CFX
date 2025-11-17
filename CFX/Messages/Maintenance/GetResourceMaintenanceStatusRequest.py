from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Resource import Resource
from CFX.Messages.Structures.ResourceInformation import ResourceInformation


@dataclass_json
@dataclass
class GetResourceMaintenanceStatusRequest(CFXMessage):
    Machine: Resource
    ResourceMaintenanceDetails: List[ResourceInformation]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, machine: Resource = None, resource_maintenance_details: List[ResourceInformation] = None):
        super().__init__()
        self.type = "CFX.Maintenance.GetResourceMaintenanceStatusRequest,CFX"
        self.message_name = "CFX.Maintenance.GetResourceMaintenanceStatusRequest"
        self.Machine = machine or Resource()
        self.ResourceMaintenanceDetails = resource_maintenance_details or []