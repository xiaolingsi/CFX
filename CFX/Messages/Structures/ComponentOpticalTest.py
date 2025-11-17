from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class ComponentOpticalTest(object):
    """
    Describes details on an optical test of a component
    """
    
    ExpectedValue: float = 0.0
    MeasuredValue: float = 0.0
    ToleranceMin: float = 0.0
    ToleranceMax: float = 0.0
    Unit: Optional[str] = None
    Result: bool = False

    def __init__(self):
        pass