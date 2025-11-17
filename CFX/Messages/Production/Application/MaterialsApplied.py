import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.InstalledMaterial import InstalledMaterial


@dataclass_json
@dataclass
class MaterialsApplied(CFXMessage):
    TransactionId: uuid.UUID
    AppliedMaterials: List[InstalledMaterial]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, applied_materials: List[InstalledMaterial] = None):
        super().__init__()
        self.type = "CFX.Production.Application.MaterialsApplied,CFX"
        self.message_name = "CFX.Production.Application.MaterialsApplied"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.AppliedMaterials = applied_materials or []