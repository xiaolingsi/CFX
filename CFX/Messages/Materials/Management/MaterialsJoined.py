from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialPackage import MaterialPackage


@dataclass_json
@dataclass
class MaterialsJoined(CFXMessage):
    LeadingMaterialPackage: MaterialPackage
    TrailingMaterialPackage: MaterialPackage

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, leading_material_package: MaterialPackage = None, 
                 trailing_material_package: MaterialPackage = None):
        super().__init__()
        self.type = "CFX.Materials.Management.MaterialsJoined,CFX"
        self.message_name = "CFX.Materials.Management.MaterialsJoined"
        self.LeadingMaterialPackage = leading_material_package or MaterialPackage()
        self.TrailingMaterialPackage = trailing_material_package or MaterialPackage()
