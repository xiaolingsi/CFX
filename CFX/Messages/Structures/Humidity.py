from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.EnvironmentalCondition import EnvironmentalCondition


@dataclass_json
@dataclass
class Humidity(EnvironmentalCondition):
    """
    Describes humidity conditions
    """
    
    pass