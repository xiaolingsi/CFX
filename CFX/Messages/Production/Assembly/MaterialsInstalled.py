import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.InstalledMaterial import InstalledMaterial


@dataclass_json
@dataclass
class MaterialsInstalled(CFXMessage):
    TransactionId: str
    InstalledMaterials: List[InstalledMaterial]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", installed_materials: List[InstalledMaterial] = None):
        super().__init__()
        self.type = "CFX.Production.Assembly.MaterialsInstalled,CFX"
        self.message_name = "CFX.Production.Assembly.MaterialsInstalled"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.InstalledMaterials = installed_materials or []