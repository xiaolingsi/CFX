from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class GetAvailableRecipesRequest(CFXMessage):
    Path: str
    MaxCount: int

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, path: str = "", max_count: int = 0):
        super().__init__()
        self.type = "CFX.Production.GetAvailableRecipesRequest,CFX"
        self.message_name = "CFX.Production.GetAvailableRecipesRequest"
        self.Path = path
        self.MaxCount = max_count