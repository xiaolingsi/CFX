from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .Measurement import Measurement


@dataclass_json
@dataclass
class TextMeasurement(Measurement):
    """
    Describes a measurement that was made by a human or by automated equipment
    in the course of inspecting or testing a production unit in which the result
    of the measurement is a text based value.
    """
    
    # The actual resulting value of this text based measurement
    Value: str = ""
    
    # The expected value of this text based measurement
    ExpectedValue: str = ""