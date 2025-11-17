from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Union
from CFX.Messages.Structures.Geometry.Vector3 import Vector3


@dataclass_json
@dataclass
class Quaternion:
    """
    An efficient mathematical representation for three dimensional rotations.
    """
    
    X: float = 0.0
    Y: float = 0.0
    Z: float = 0.0
    W: float = 1.0
    
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 1.0):
        self.X = x
        self.Y = y
        self.Z = z
        self.W = w
    
    def __add__(self, other: 'Quaternion') -> 'Quaternion':
        return Quaternion(self.X + other.X, self.Y + other.Y, self.Z + other.Z, self.W + other.W)
    
    def __sub__(self, other: 'Quaternion') -> 'Quaternion':
        return Quaternion(self.X - other.X, self.Y - other.Y, self.Z - other.Z, self.W - other.W)
    
    def __mul__(self, other: Union['Quaternion', float]) -> 'Quaternion':
        if isinstance(other, Quaternion):
            # Quaternion multiplication
            return Quaternion(
                self.W * other.X + self.X * other.W + self.Y * other.Z - self.Z * other.Y,
                self.W * other.Y + self.Y * other.W + self.Z * other.X - self.X * other.Z,
                self.W * other.Z + self.Z * other.W + self.X * other.Y - self.Y * other.X,
                self.W * other.W - self.X * other.X - self.Y * other.Y - self.Z * other.Z
            )
        else:
            # Scalar multiplication
            return Quaternion(self.X * other, self.Y * other, self.Z * other, self.W * other)
    
    def length(self) -> float:
        return (self.X**2 + self.Y**2 + self.Z**2 + self.W**2)**0.5
    
    def normalize(self) -> 'Quaternion':
        length = self.length()
        if length > 0:
            return Quaternion(self.X / length, self.Y / length, self.Z / length, self.W / length)
        return Quaternion()
    
    def conjugate(self) -> 'Quaternion':
        return Quaternion(-self.X, -self.Y, -self.Z, self.W)
    
    def inverse(self) -> 'Quaternion':
        length_sq = self.X**2 + self.Y**2 + self.Z**2 + self.W**2
        if length_sq > 0:
            return self.conjugate() * (1.0 / length_sq)
        return Quaternion()
    
    @staticmethod
    def create_from_axis_angle(axis: Vector3, angle: float) -> 'Quaternion':
        """Create a quaternion from axis-angle representation"""
        half_angle = angle * 0.5
        sin_half = math.sin(half_angle)
        cos_half = math.cos(half_angle)
        
        axis_normalized = axis.normalize()
        return Quaternion(
            axis_normalized.X * sin_half,
            axis_normalized.Y * sin_half,
            axis_normalized.Z * sin_half,
            cos_half
        )
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quaternion):
            return False
        return (abs(self.X - other.X) < 1e-10 and 
                abs(self.Y - other.Y) < 1e-10 and 
                abs(self.Z - other.Z) < 1e-10 and 
                abs(self.W - other.W) < 1e-10)
    
    def __str__(self) -> str:
        return f"{{X:{self.X} Y:{self.Y} Z:{self.Z} W:{self.W}}}"


# Static properties
Quaternion.identity = Quaternion(0.0, 0.0, 0.0, 1.0)

# Import math for trigonometric functions
import math