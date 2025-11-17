from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialLocation import MaterialLocation


@dataclass_json
@dataclass
class MaterialsEmpty(CFXMessage):
    EmptyMaterials: List[MaterialLocation]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, empty_materials: List[MaterialLocation] = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.MaterialsEmpty,CFX"
        self.message_name = "CFX.Materials.Storage.MaterialsEmpty"
        self.EmptyMaterials = empty_materials or []