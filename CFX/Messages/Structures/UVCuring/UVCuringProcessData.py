from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from .. import ProcessData, NumericMeasurement
from .UVCuringLampData import UVCuringLampData
from .UVCuringGlassPlate import UVCuringGlassPlate

@dataclass_json
@dataclass
class UVCuringProcessData(ProcessData):
    """
    UV Curing Process Data
    ** NOTE: ADDED in CFX 1.6 **
    """
    def __init__(self):
        super().__init__()
        self.uv_lamps: List[UVCuringLampData] = []

    process_time: NumericMeasurement
    conveyor_speed: NumericMeasurement
    conveyor_width: NumericMeasurement
    intensity: NumericMeasurement
    uv_lamps: List[UVCuringLampData]
    glass_plates: List[UVCuringGlassPlate]