from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ConsumedMaterial import ConsumedMaterial


@dataclass_json
@dataclass
class MaterialsConsumed(CFXMessage):
    ConsumedMaterials: List[ConsumedMaterial]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, consumed_materials: List[ConsumedMaterial] = None):
        super().__init__()
        self.type = "CFX.Materials.Management.MaterialsConsumed,CFX"
        self.message_name = "CFX.Materials.Management.MaterialsConsumed"
        self.ConsumedMaterials = consumed_materials or []
