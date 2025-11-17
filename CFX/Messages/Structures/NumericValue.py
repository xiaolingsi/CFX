from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class NumericValue:
    """A data structure that represents a numeric value with defined units and thresholds"""
    
    # The actual numeric value that was measured and recorded during a test or inspection
    Value: float = 0.0
    
    # The units of the value (must be a valid SI unit)
    ValueUnits: Optional[str] = None
    
    # The expected value for thie measurement
    ExpectedValue: Optional[float] = None
    
    # The units of the expected value (must be a valid SI unit)
    ExpectedValueUnits: Optional[str] = None
    
    # The minimum acceptable value
    MinimumAcceptableValue: Optional[float] = None
    
    # The maximum acceptable value
    MaximumAcceptableValue: Optional[float] = None