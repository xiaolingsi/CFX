from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialPackageDetail import MaterialPackageDetail
from CFX.Messages.Structures.MaterialModifyReason import MaterialModifyReason


@dataclass_json
@dataclass
class MaterialsModified(CFXMessage):
    Reason: MaterialModifyReason
    Materials: List[MaterialPackageDetail]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, reason: MaterialModifyReason = None, materials: List[MaterialPackageDetail] = None):
        super().__init__()
        self.type = "CFX.Materials.Management.MaterialsModified,CFX"
        self.message_name = "CFX.Materials.Management.MaterialsModified"
        self.Reason = reason or MaterialModifyReason.Unspecified
        self.Materials = materials or []