from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .EnvironmentalCondition import EnvironmentalCondition


@dataclass_json
@dataclass
class Temperature(EnvironmentalCondition):
    """
    A type of environmental condition that represents thermal level
    """
    pass