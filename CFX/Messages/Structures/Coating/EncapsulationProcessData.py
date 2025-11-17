from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Coating.CoatingProcessData import CoatingProcessData


@dataclass_json
@dataclass
class EncapsulationProcessData(CoatingProcessData):
    """
    A dynamic data structure representing data that was collected during an encapsulation process.
    """
    
    def __init__(self, readings=None, nozzle=None):
        super().__init__(readings, nozzle)