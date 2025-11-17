from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class UnblockMaterialsRequest(CFXMessage):
    MaterialPackageIdentifiers: List[str]
    Comments: str
    Unblocker: Operator

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, material_package_identifiers: List[str] = None, comments: str = "", 
                 unblocker: Operator = None):
        super().__init__()
        self.type = "CFX.Materials.Management.UnblockMaterialsRequest,CFX"
        self.message_name = "CFX.Materials.Management.UnblockMaterialsRequest"
        self.MaterialPackageIdentifiers = material_package_identifiers or []
        self.Comments = comments
        self.Unblocker = unblocker or Operator()