from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Coating.CoatingNozzle import CoatingNozzle
from CFX.Messages.Structures.Coating.CoatingMeasurement import CoatingMeasurement


@dataclass_json
@dataclass
class CoatingNozzleData(object):
    """
    Provides information about the conditions of a particular Nozzle of a Coating machine at a given point in time.
    NOTE: ADDED in CFX 1.5
    """
    
    # Coating Nozzle to which this coating data is related.
    Nozzle: Optional[CoatingNozzle] = None
    
    # A list of readings / measurements that have been taken for this Nozzle.
    NozzleReadings: List[CoatingMeasurement] = field(default_factory=list)
    
    def __init__(self, nozzle=None, nozzleReadings=None):
        self.Nozzle = nozzle
        self.NozzleReadings = nozzleReadings if nozzleReadings is not None else []