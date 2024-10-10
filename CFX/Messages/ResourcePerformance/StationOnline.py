from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class StationOnline(CFXMessage):
    OfflineDuration:str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,offline_duration):
        super().__init__()
        self.type = "CFX.ResourcePerformance.StationOnline,CFX"
        self.message_name = "CFX.ResourcePerformance.StationOnline"
        self.OfflineDuration = offline_duration


if __name__ == '__main__':
    station_online = StationOnline("00:05:00")
    print(station_online.to_cfx_json())