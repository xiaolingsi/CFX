from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Union


@dataclass_json
@dataclass
class Vector3:
    """
    Describes a 3D-vector.
    """
    
    X: float = 0.0
    Y: float = 0.0
    Z: float = 0.0
    
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.X = x
        self.Y = y
        self.Z = z
    
    def __add__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.X + other.X, self.Y + other.Y, self.Z + other.Z)
    
    def __sub__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.X - other.X, self.Y - other.Y, self.Z - other.Z)
    
    def __mul__(self, scalar: float) -> 'Vector3':
        return Vector3(self.X * scalar, self.Y * scalar, self.Z * scalar)
    
    def __truediv__(self, scalar: float) -> 'Vector3':
        return Vector3(self.X / scalar, self.Y / scalar, self.Z / scalar)
    
    def __mod__(self, other: 'Vector3') -> 'Vector3':
        """Modulo operation for Vector3"""
        return Vector3(self.X % other.X, self.Y % other.Y, self.Z % other.Z)
    
    def length(self) -> float:
        return (self.X**2 + self.Y**2 + self.Z**2)**0.5
    
    def normalize(self) -> 'Vector3':
        length = self.length()
        if length > 0:
            return Vector3(self.X / length, self.Y / length, self.Z / length)
        return Vector3()
    
    def dot(self, other: 'Vector3') -> float:
        return self.X * other.X + self.Y * other.Y + self.Z * other.Z
    
    def cross(self, other: 'Vector3') -> 'Vector3':
        return Vector3(
            self.Y * other.Z - self.Z * other.Y,
            self.Z * other.X - self.X * other.Z,
            self.X * other.Y - self.Y * other.X
        )
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector3):
            return False
        return (abs(self.X - other.X) < 1e-10 and 
                abs(self.Y - other.Y) < 1e-10 and 
                abs(self.Z - other.Z) < 1e-10)
    
    def __str__(self) -> str:
        return f"{{X:{self.X} Y:{self.Y} Z:{self.Z}}}"


# Static properties
Vector3.zero = Vector3(0.0, 0.0, 0.0)
Vector3.unit_x = Vector3(1.0, 0.0, 0.0)
Vector3.unit_y = Vector3(0.0, 1.0, 0.0)
Vector3.unit_z = Vector3(0.0, 0.0, 1.0)