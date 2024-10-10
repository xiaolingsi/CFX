from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class UnitPosition(object):
    UnitIdentifier: str
    PositionNumber: int
    PositionName: str
    X: float
    Y: float
    Rotation: float
    FlipX: bool
    FlipY: bool

    def __init__(self, UnitIdentifier="", PositionNumber=0, PositionName="", X:float=0.0, Y:float=0.0, Rotation:float=0.0, FlipX:bool=0.0, FlipY:bool=0.0):
        self.UnitIdentifier = UnitIdentifier
        self.PositionNumber = PositionNumber
        self.PositionName = PositionName
        self.X = X
        self.Y = Y
        self.Rotation = Rotation
        self.FlipX = FlipX
        self.FlipY = FlipY


