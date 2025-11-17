from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .. import Measurement

@dataclass_json
@dataclass
class CoatingThicknessMeasurement(Measurement):
    """
    Structure base class representing slide position.
    Average coating thickness measured in micrometers.
    ** NOTE: ADDED in CFX 1.2 **
    """
    position: int
    thickness: float