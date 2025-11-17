from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.Resource import Resource
from CFX.Messages.Structures.Maintenance.ServiceAndMaintenanceData import ServiceAndMaintenanceData


@dataclass_json
@dataclass
class GetResourceMaintenanceAndServiceResponse(CFXMessage):
    Result: RequestResult
    Machine: Resource
    MachineServiceAndMaintenanceData: List[ServiceAndMaintenanceData]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, machine: Resource = None, 
                 machine_service_and_maintenance_data: List[ServiceAndMaintenanceData] = None):
        super().__init__()
        self.type = "CFX.Maintenance.GetResourceMaintenanceAndServiceResponse,CFX"
        self.message_name = "CFX.Maintenance.GetResourceMaintenanceAndServiceResponse"
        self.Result = result or RequestResult()
        self.Machine = machine or Resource()
        self.MachineServiceAndMaintenanceData = machine_service_and_maintenance_data or []