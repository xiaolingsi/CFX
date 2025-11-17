from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Measurement import Measurement


@dataclass_json
@dataclass
class BooleanMeasurement(Measurement):
    """
    Describes a measurement that was made by a human or by automated equipment
    in the course of inspecting or testing a production unit in which the result
    of the measurement is a boolean (true / false) value.
    """
    
    Value: bool = False
    ExpectedValue: bool = False