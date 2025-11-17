from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ComponentOpticalTest import ComponentOpticalTest


@dataclass_json
@dataclass
class BadOpticalTestRejectionDetails(ComponentOpticalTest):
    """
    Describes details on a bad optical test
    """
    
    def __init__(self):
        super().__init__()
        self.Result = False