from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialPackage import MaterialPackage


@dataclass_json
@dataclass
class MaterialsChainSplit(CFXMessage):
    SplittedMaterialPackage: MaterialPackage
    RemainingMaterialPackage: MaterialPackage

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, splitted_material_package: MaterialPackage = None, 
                 remaining_material_package: MaterialPackage = None):
        super().__init__()
        self.type = "CFX.Materials.Management.MaterialsChainSplit,CFX"
        self.message_name = "CFX.Materials.Management.MaterialsChainSplit"
        self.SplittedMaterialPackage = splitted_material_package or MaterialPackage()
        self.RemainingMaterialPackage = remaining_material_package or MaterialPackage()
