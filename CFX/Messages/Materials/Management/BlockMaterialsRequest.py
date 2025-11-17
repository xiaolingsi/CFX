from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.BlockReason import BlockReason


@dataclass_json
@dataclass
class BlockMaterialsRequest(CFXMessage):
    MaterialPackageIdentifiers: List[str]
    Reason: BlockReason
    Comments: str
    Blocker: Operator

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, material_package_identifiers: List[str] = None, reason: BlockReason = None, 
                 comments: str = "", blocker: Operator = None):
        super().__init__()
        self.type = "CFX.Materials.Management.BlockMaterialsRequest,CFX"
        self.message_name = "CFX.Materials.Management.BlockMaterialsRequest"
        self.MaterialPackageIdentifiers = material_package_identifiers or []
        self.Reason = reason or BlockReason.Defective
        self.Comments = comments
        self.Blocker = blocker or Operator()