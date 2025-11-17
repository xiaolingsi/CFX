import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UninstalledMaterial import UninstalledMaterial


@dataclass_json
@dataclass
class MaterialsUninstalled(CFXMessage):
    TransactionId: str
    UninstalledMaterials: List[UninstalledMaterial]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", uninstalled_materials: List[UninstalledMaterial] = None):
        super().__init__()
        self.type = "CFX.Production.Assembly.MaterialsUninstalled,CFX"
        self.message_name = "CFX.Production.Assembly.MaterialsUninstalled"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.UninstalledMaterials = uninstalled_materials or []