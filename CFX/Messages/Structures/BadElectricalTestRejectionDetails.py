from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ComponentElectricalTest import ComponentElectricalTest


@dataclass_json
@dataclass
class BadElectricalTestRejectionDetails(ComponentElectricalTest):
    """
    Describes details on an bad electrical test of a component
    """
    
    def __init__(self):
        super().__init__()
        self.Result = False