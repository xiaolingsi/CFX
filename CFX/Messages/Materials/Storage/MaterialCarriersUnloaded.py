from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class MaterialCarriersUnloaded(CFXMessage):
    CarrierIdentifiers: List[str]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, carrier_identifiers: List[str] = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.MaterialCarriersUnloaded,CFX"
        self.message_name = "CFX.Materials.Storage.MaterialCarriersUnloaded"
        self.CarrierIdentifiers = carrier_identifiers or []