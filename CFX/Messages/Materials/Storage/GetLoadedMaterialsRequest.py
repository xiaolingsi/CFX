from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class GetLoadedMaterialsRequest(CFXMessage):
    LocationIdentifiers: List[str]
    ResourceUniqueIdentifier: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, location_identifiers: List[str] = None, resource_unique_identifier: str = ""):
        super().__init__()
        self.type = "CFX.Materials.Storage.GetLoadedMaterialsRequest,CFX"
        self.message_name = "CFX.Materials.Storage.GetLoadedMaterialsRequest"
        self.LocationIdentifiers = location_identifiers or []
        self.ResourceUniqueIdentifier = resource_unique_identifier