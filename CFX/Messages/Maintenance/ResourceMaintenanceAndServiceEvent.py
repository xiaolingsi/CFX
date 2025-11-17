from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from datetime import datetime
from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.Resource import Resource
from CFX.Messages.Structures.Maintenance.ServiceAndMaintenanceData import ServiceAndMaintenanceData


@dataclass_json
@dataclass
class ResourceMaintenanceAndServiceEvent(CFXMessage):
    EventDateTime: datetime
    Machine: Resource
    MachineServiceAndMaintenanceData: List[ServiceAndMaintenanceData]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, event_datetime: datetime = None, machine: Resource = None, 
                 machine_service_and_maintenance_data: List[ServiceAndMaintenanceData] = None):
        super().__init__()
        self.type = "CFX.Maintenance.ResourceMaintenanceAndServiceEvent,CFX"
        self.message_name = "CFX.Maintenance.ResourceMaintenanceAndServiceEvent"
        self.EventDateTime = event_datetime or CFXUtils.get_iso8601_time()
        self.Machine = machine or Resource()
        self.MachineServiceAndMaintenanceData = machine_service_and_maintenance_data or []