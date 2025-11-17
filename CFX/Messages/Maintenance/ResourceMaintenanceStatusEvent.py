from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from datetime import datetime
from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.Resource import Resource
from CFX.Messages.Structures.ResourceInformation import ResourceInformation


@dataclass_json
@dataclass
class ResourceMaintenanceStatusEvent(CFXMessage):
    EventDateTime: datetime
    Machine: Resource
    ResourceMaintenanceDetails: List[ResourceInformation]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, event_datetime: datetime = None, machine: Resource = None,
                 resource_maintenance_details: List[ResourceInformation] = None):
        super().__init__()
        self.type = "CFX.Maintenance.ResourceMaintenanceStatusEvent,CFX"
        self.message_name = "CFX.Maintenance.ResourceMaintenanceStatusEvent"
        self.EventDateTime = event_datetime or CFXUtils.get_iso8601_time()
        self.Machine = machine or Resource()
        self.ResourceMaintenanceDetails = resource_maintenance_details or []