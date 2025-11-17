from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class UVCuringGlassPlate:
    """
    Properties of glass plate.
    ** NOTE: ADDED in CFX 1.6 **
    """
    row: int
    is_present: bool