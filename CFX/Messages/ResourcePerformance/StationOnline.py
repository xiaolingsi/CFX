from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class StationOnline(CFXMessage):
    OfflineDuration: Optional[str] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, offline_duration=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.StationOnline,CFX"
        self.message_name = "CFX.ResourcePerformance.StationOnline"
        self.OfflineDuration = offline_duration
