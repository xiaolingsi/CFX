from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class ValidateStationSetupResponse(CFXMessage):
    Result: RequestResult

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.ValidateStationSetupResponse,CFX"
        self.message_name = "CFX.Materials.Storage.ValidateStationSetupResponse"
        self.Result = result or RequestResult()