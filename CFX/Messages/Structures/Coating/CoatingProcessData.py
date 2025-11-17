from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ProcessData import ProcessData
from CFX.Messages.Structures.Coating.CoatingMeasurement import CoatingMeasurement
from CFX.Messages.Structures.Coating.CoatingNozzleData import CoatingNozzleData


@dataclass_json
@dataclass
class CoatingProcessData(ProcessData):
    """
    A dynamic data structure representing data that was collected during a coating process.
    """
    
    # A list of measurements that were taken in the course of the coating or encapsulation operation.
    Readings: List[CoatingMeasurement] = field(default_factory=list)
    
    # Process data (temperatures, etc.) for each Nozzle of the Coating machine at the 
    # time when this transaction tool place.
    # NOTE: ADDED in CFX 1.5
    Nozzle: List[CoatingNozzleData] = field(default_factory=list)
    
    def __init__(self, readings=None, nozzle=None):
        super().__init__()
        self.Readings = readings if readings is not None else []
        self.Nozzle = nozzle if nozzle is not None else []