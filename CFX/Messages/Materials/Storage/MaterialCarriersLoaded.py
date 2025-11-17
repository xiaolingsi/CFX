from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialCarrierLocation import MaterialCarrierLocation


@dataclass_json
@dataclass
class MaterialCarriersLoaded(CFXMessage):
    Carriers: List[MaterialCarrierLocation]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, carriers: List[MaterialCarrierLocation] = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.MaterialCarriersLoaded,CFX"
        self.message_name = "CFX.Materials.Storage.MaterialCarriersLoaded"
        self.Carriers = carriers or []