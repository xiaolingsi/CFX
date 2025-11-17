from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Union


@dataclass_json
@dataclass
class Vector4:
    """
    Describes a 4D-vector.
    """
    
    X: float = 0.0
    Y: float = 0.0
    Z: float = 0.0
    W: float = 0.0
    
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0):
        self.X = x
        self.Y = y
        self.Z = z
        self.W = w
    
    def __add__(self, other: 'Vector4') -> 'Vector4':
        return Vector4(self.X + other.X, self.Y + other.Y, self.Z + other.Z, self.W + other.W)
    
    def __sub__(self, other: 'Vector4') -> 'Vector4':
        return Vector4(self.X - other.X, self.Y - other.Y, self.Z - other.Z, self.W - other.W)
    
    def __mul__(self, scalar: float) -> 'Vector4':
        return Vector4(self.X * scalar, self.Y * scalar, self.Z * scalar, self.W * scalar)
    
    def __truediv__(self, scalar: float) -> 'Vector4':
        return Vector4(self.X / scalar, self.Y / scalar, self.Z / scalar, self.W / scalar)
    
    def length(self) -> float:
        return (self.X**2 + self.Y**2 + self.Z**2 + self.W**2)**0.5
    
    def normalize(self) -> 'Vector4':
        length = self.length()
        if length > 0:
            return Vector4(self.X / length, self.Y / length, self.Z / length, self.W / length)
        return Vector4()
    
    def dot(self, other: 'Vector4') -> float:
        return self.X * other.X + self.Y * other.Y + self.Z * other.Z + self.W * other.W
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector4):
            return False
        return (abs(self.X - other.X) < 1e-10 and 
                abs(self.Y - other.Y) < 1e-10 and 
                abs(self.Z - other.Z) < 1e-10 and 
                abs(self.W - other.W) < 1e-10)
    
    def __str__(self) -> str:
        return f"{{X:{self.X} Y:{self.Y} Z:{self.Z} W:{self.W}}}"


# Static properties
Vector4.zero = Vector4(0.0, 0.0, 0.0, 0.0)
Vector4.unit_x = Vector4(1.0, 0.0, 0.0, 0.0)
Vector4.unit_y = Vector4(0.0, 1.0, 0.0, 0.0)
Vector4.unit_z = Vector4(0.0, 0.0, 1.0, 0.0)
Vector4.unit_w = Vector4(0.0, 0.0, 0.0, 1.0)