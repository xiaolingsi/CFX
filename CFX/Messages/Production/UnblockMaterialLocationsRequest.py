from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialLocation import MaterialLocation


@dataclass_json
@dataclass
class UnblockMaterialLocationsRequest(CFXMessage):
    Locations: List[MaterialLocation]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, locations: List[MaterialLocation] = None):
        super().__init__()
        self.type = "CFX.Production.UnblockMaterialLocationsRequest,CFX"
        self.message_name = "CFX.Production.UnblockMaterialLocationsRequest"
        self.Locations = locations or []