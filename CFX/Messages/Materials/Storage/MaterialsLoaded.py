from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialLocation import MaterialLocation


@dataclass_json
@dataclass
class MaterialsLoaded(CFXMessage):
    Materials: List[MaterialLocation]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, materials: List[MaterialLocation] = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.MaterialsLoaded,CFX"
        self.message_name = "CFX.Materials.Storage.MaterialsLoaded"
        self.Materials = materials or []