from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.StationSetupRequirements import StationSetupRequirements


@dataclass_json
@dataclass
class ValidateStationSetupRequest(CFXMessage):
    SetupRequirements: StationSetupRequirements

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, setup_requirements: StationSetupRequirements = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.ValidateStationSetupRequest,CFX"
        self.message_name = "CFX.Materials.Storage.ValidateStationSetupRequest"
        self.SetupRequirements = setup_requirements or StationSetupRequirements()