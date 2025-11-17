from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.Messages.Structures.ComponentVisionTest import ComponentVisionTest


@dataclass_json
@dataclass
class BadVisionTestRejectionDetails(List[ComponentVisionTest]):
    """
    Describes details on a bad vision test
    """
    
    def __init__(self):
        super().__init__()