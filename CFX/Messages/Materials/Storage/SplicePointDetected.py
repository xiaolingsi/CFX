from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.MaterialLocation import MaterialLocation


@dataclass_json
@dataclass
class SplicePointDetected(CFXMessage):
    DepletedMaterial: MaterialLocation
    NewlyActiveMaterial: MaterialLocation

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, depleted_material: MaterialLocation = None, newly_active_material: MaterialLocation = None):
        super().__init__()
        self.type = "CFX.Materials.Storage.SplicePointDetected,CFX"
        self.message_name = "CFX.Materials.Storage.SplicePointDetected"
        self.DepletedMaterial = depleted_material or MaterialLocation()
        self.NewlyActiveMaterial = newly_active_material or MaterialLocation()