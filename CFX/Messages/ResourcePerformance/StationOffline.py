from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class StationOffline(CFXMessage):

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self):
        super().__init__()
        self.type = "CFX.ResourcePerformance.StationOffline,CFX"
        self.message_name = "CFX.ResourcePerformance.StationOffline"


