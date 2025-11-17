from CFX.CFXMessage import CFXMessage
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.Structures.Endpoint import Endpoint
from CFX.Messages.Structures.StageInformation import StageInformation
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StatusResult import StatusResult
from CFX.Messages.genericUnits.SupportedTopic import SupportedTopic


@dataclass_json
@dataclass
class GetEndpointInformationResponse(CFXMessage):
    EndpointInformation:Endpoint
    Result:RequestResult

    def __init__(self, endpoint_information:Endpoint,result:RequestResult):
        super().__init__()
        self.type = "CFX.GetEndpointInformationResponse,CFX"
        self.message_name = "CFX.GetEndpointInformationResponse"
        self.EndpointInformation = endpoint_information
        self.Result = result

    def to_cfx_json(self):
        return self.to_json()

