from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialLocation import MaterialLocation
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class GetLoadedMaterialsResponse(CFXMessage):
    Result: RequestResult
    Materials: List[MaterialLocation]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, materials: List[MaterialLocation] = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.GetLoadedMaterialsResponse,CFX"
        self.message_name = "CFX.Materials.Storage.GetLoadedMaterialsResponse"
        self.Result = result or RequestResult()
        self.Materials = materials or []