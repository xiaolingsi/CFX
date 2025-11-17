from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .UVCuringLampState import UVCuringLampState

@dataclass_json
@dataclass
class UVCuringLampData:
    """
    Properties of an UV lamp.
    ** NOTE: ADDED in CFX 1.6 **
    """
    row: int
    column: int
    uv_curing_lamp_state: UVCuringLampState