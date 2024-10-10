from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Fault import Fault
from CFX.Messages.Structures.ResourceState import ResourceState


@dataclass_json
@dataclass
class StationStateChanged(CFXMessage):
    NewState: ResourceState
    OldState: ResourceState
    OldStateDuration: str
    RelatedFault: Fault

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, old_state_duration="00:00:00",
                 new_state: ResourceState = ResourceState.PRD,
                 old_state: ResourceState = ResourceState.PRD):
        super().__init__()
        self.type = "CFX.ResourcePerformance.StationStateChanged,CFX"
        self.message_name = "CFX.ResourcePerformance.StationStateChanged"
        self.OldStateDuration = old_state_duration
        self.NewState = new_state
        self.OldState = old_state
        self.RelatedFault = None


if __name__ == '__main__':
    stationStateChanged = StationStateChanged("00:05:00")
    print(stationStateChanged.to_cfx_json())
