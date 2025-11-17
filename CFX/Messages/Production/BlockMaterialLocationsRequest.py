from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialLocation import MaterialLocation
from CFX.Messages.Structures.BlockReason import BlockReason


@dataclass_json
@dataclass
class BlockMaterialLocationsRequest(CFXMessage):
    Reason: BlockReason
    Comments: str
    Locations: List[MaterialLocation]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, reason: BlockReason = None, comments: str = "", locations: List[MaterialLocation] = None):
        super().__init__()
        self.type = "CFX.Production.BlockMaterialLocationsRequest,CFX"
        self.message_name = "CFX.Production.BlockMaterialLocationsRequest"
        self.Reason = reason or BlockReason.Unspecified
        self.Comments = comments
        self.Locations = locations or []