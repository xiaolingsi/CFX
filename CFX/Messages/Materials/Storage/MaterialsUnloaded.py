from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class MaterialsUnloaded(CFXMessage):
    MaterialPackageIdentifiers: List[str]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, material_package_identifiers: List[str] = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.MaterialsUnloaded,CFX"
        self.message_name = "CFX.Materials.Storage.MaterialsUnloaded"
        self.MaterialPackageIdentifiers = material_package_identifiers or []