from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class MaterialsSplit(CFXMessage):
    SourceMaterialPackageIdentifier: str
    SourceMaterialPackageRemainingQuantity: float
    NewMaterialPackageIdentifier: str
    NewMaterialPackageQuantity: float

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, source_material_package_identifier: str = "", 
                 source_material_package_remaining_quantity: float = 0.0, 
                 new_material_package_identifier: str = "", 
                 new_material_package_quantity: float = 0.0):
        super().__init__()
        self.type = "CFX.Materials.Management.MaterialsSplit,CFX"
        self.message_name = "CFX.Materials.Management.MaterialsSplit"
        self.SourceMaterialPackageIdentifier = source_material_package_identifier
        self.SourceMaterialPackageRemainingQuantity = source_material_package_remaining_quantity
        self.NewMaterialPackageIdentifier = new_material_package_identifier
        self.NewMaterialPackageQuantity = new_material_package_quantity