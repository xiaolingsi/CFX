from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class BlockMaterialsResponse(CFXMessage):
    Result: RequestResult
    MaterialsPackagesNotBlocked: List[str]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, materials_packages_not_blocked: List[str] = None):
        super().__init__()
        self.type = "CFX.Materials.Management.BlockMaterialsResponse,CFX"
        self.message_name = "CFX.Materials.Management.BlockMaterialsResponse"
        self.Result = result or RequestResult()
        self.MaterialsPackagesNotBlocked = materials_packages_not_blocked or []