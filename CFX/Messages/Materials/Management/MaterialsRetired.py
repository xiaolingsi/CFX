from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialPackage import MaterialPackage


@dataclass_json
@dataclass
class MaterialsRetired(CFXMessage):
    Materials: List[MaterialPackage]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, materials: List[MaterialPackage] = None):
        super().__init__()
        self.type = "CFX.Materials.Management.MaterialsRetired,CFX"
        self.message_name = "CFX.Materials.Management.MaterialsRetired"
        self.Materials = materials or []