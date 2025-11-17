from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .Measurement import Measurement
from .NumericValue import NumericValue

@dataclass_json
@dataclass
class NumericMeasurement(Measurement):
    """Describes a numeric (floating point) measurement that was made by a human or by automated equipment
    in the course of inspecting or testing a production unit"""
    
    def __init__(self):
        super().__init__()
        self.MeasuredValue = NumericValue()
    
    # The actual numeric value measured and recorded during this test/inspection.
    MeasuredValue: Optional[NumericValue] = None