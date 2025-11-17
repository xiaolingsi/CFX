from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class UnitPosition(object):

    UnitIdentifier: Optional[str] = None
    PositionNumber: Optional[int] = 0
    PositionName: Optional[str] = None
    X: Optional[float] = 0.0
    Y: Optional[float] = 0.0
    Rotation: Optional[float] = 0.0
    FlipX: Optional[bool] = False
    FlipY:  Optional[bool] = False

    def __init__(self, UnitIdentifier="", PositionNumber=0, PositionName="", X:float=0.0, Y:float=0.0, Rotation:float=0.0, FlipX:bool=0.0, FlipY:bool=0.0):
        self.UnitIdentifier = UnitIdentifier or ""
        self.PositionNumber = PositionNumber
        self.PositionName = PositionName
        self.X = X
        self.Y = Y
        self.Rotation = Rotation
        self.FlipX = FlipX
        self.FlipY = FlipY


