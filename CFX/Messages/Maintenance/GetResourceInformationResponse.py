from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.Resource import Resource


@dataclass_json
@dataclass
class GetResourceInformationResponse(CFXMessage):
    Result: RequestResult
    ResourceInformation: Resource

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, resource_information: Resource = None):
        super().__init__()
        self.type = "CFX.Maintenance.GetResourceInformationResponse,CFX"
        self.message_name = "CFX.Maintenance.GetResourceInformationResponse"
        self.Result = result or RequestResult()
        self.ResourceInformation = resource_information or Resource()