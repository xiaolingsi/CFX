from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Union


@dataclass_json
@dataclass
class Vector2:
    """
    Describes a 2D-vector.
    """
    
    X: float = 0.0
    Y: float = 0.0
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.X = x
        self.Y = y
    
    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.X + other.X, self.Y + other.Y)
    
    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.X - other.X, self.Y - other.Y)
    
    def __mul__(self, scalar: float) -> 'Vector2':
        return Vector2(self.X * scalar, self.Y * scalar)
    
    def __truediv__(self, scalar: float) -> 'Vector2':
        return Vector2(self.X / scalar, self.Y / scalar)
    
    def length(self) -> float:
        return (self.X**2 + self.Y**2)**0.5
    
    def normalize(self) -> 'Vector2':
        length = self.length()
        if length > 0:
            return Vector2(self.X / length, self.Y / length)
        return Vector2()
    
    def dot(self, other: 'Vector2') -> float:
        return self.X * other.X + self.Y * other.Y
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2):
            return False
        return abs(self.X - other.X) < 1e-10 and abs(self.Y - other.Y) < 1e-10
    
    def __str__(self) -> str:
        return f"{{X:{self.X} Y:{self.Y}}}"


# Static properties
Vector2.zero = Vector2(0.0, 0.0)
Vector2.unit_x = Vector2(1.0, 0.0)
Vector2.unit_y = Vector2(0.0, 1.0)