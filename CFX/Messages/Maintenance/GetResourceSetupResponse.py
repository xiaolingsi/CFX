from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.Resource import Resource


@dataclass_json
@dataclass
class GetResourceSetupResponse(CFXMessage):
    Result: RequestResult
    ResourceSetup: Resource

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, resource_setup: Resource = None):
        super().__init__()
        self.type = "CFX.Maintenance.GetResourceSetupResponse,CFX"
        self.message_name = "CFX.Maintenance.GetResourceSetupResponse"
        self.Result = result or RequestResult()
        self.ResourceSetup = resource_setup or Resource()