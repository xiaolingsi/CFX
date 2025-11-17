from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ComponentPressureTest import ComponentPressureTest


@dataclass_json
@dataclass
class BadPressureTestRejectionDetails(ComponentPressureTest):
    """
    Describes details on a bad pressure test
    """
    
    def __init__(self):
        super().__init__()
        self.Result = False