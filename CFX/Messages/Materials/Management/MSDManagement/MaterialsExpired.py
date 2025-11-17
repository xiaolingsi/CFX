from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialPackageDetail import MaterialPackageDetail


@dataclass_json
@dataclass
class MaterialsExpired(CFXMessage):
    Materials: List[MaterialPackageDetail]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, materials: List[MaterialPackageDetail] = None):
        super().__init__()
        self.type = "CFX.Materials.Management.MSDManagement.MaterialsExpired,CFX"
        self.message_name = "CFX.Materials.Management.MSDManagement.MaterialsExpired"
        self.Materials = materials or []