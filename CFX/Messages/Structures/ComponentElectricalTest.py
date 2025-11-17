from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from CFX.Messages.Structures.ComponentElectricalTestUnit import ComponentElectricalTestUnit


@dataclass_json
@dataclass
class ComponentElectricalTest(object):
    """
    Describes details on an electrical test of a component
    """
    
    TesterSerialNumber: Optional[str] = None
    Frequency: float = 0.0
    ExpectedValue: float = 0.0
    MeasuredValue: float = 0.0
    ToleranceMin: float = 0.0
    ToleranceMax: float = 0.0
    Unit: Optional[ComponentElectricalTestUnit] = None
    Result: bool = False

    def __init__(self):
        pass