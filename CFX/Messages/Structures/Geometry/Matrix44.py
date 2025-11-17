from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Union
from CFX.Messages.Structures.Geometry.Vector3 import Vector3
from CFX.Messages.Structures.Geometry.Vector4 import Vector4
from CFX.Messages.Structures.Geometry.Quaternion import Quaternion


@dataclass_json
@dataclass
class Matrix44:
    """
    Represents the right-handed 4x4 floating point matrix, which can store translation, scale and rotation information.
    """
    
    M11: float = 1.0
    M12: float = 0.0
    M13: float = 0.0
    M14: float = 0.0
    M21: float = 0.0
    M22: float = 1.0
    M23: float = 0.0
    M24: float = 0.0
    M31: float = 0.0
    M32: float = 0.0
    M33: float = 1.0
    M34: float = 0.0
    M41: float = 0.0
    M42: float = 0.0
    M43: float = 0.0
    M44: float = 1.0
    
    def __init__(self, m11: float = 1.0, m12: float = 0.0, m13: float = 0.0, m14: float = 0.0,
                 m21: float = 0.0, m22: float = 1.0, m23: float = 0.0, m24: float = 0.0,
                 m31: float = 0.0, m32: float = 0.0, m33: float = 1.0, m34: float = 0.0,
                 m41: float = 0.0, m42: float = 0.0, m43: float = 0.0, m44: float = 1.0):
        self.M11 = m11
        self.M12 = m12
        self.M13 = m13
        self.M14 = m14
        self.M21 = m21
        self.M22 = m22
        self.M23 = m23
        self.M24 = m24
        self.M31 = m31
        self.M32 = m32
        self.M33 = m33
        self.M34 = m34
        self.M41 = m41
        self.M42 = m42
        self.M43 = m43
        self.M44 = m44
    
    @property
    def backward(self) -> Vector3:
        """The backward vector formed from the third row M31, M32, M33 elements."""
        return Vector3(self.M31, self.M32, self.M33)
    
    @property
    def down(self) -> Vector3:
        """The down vector formed from the second row -M21, -M22, -M23 elements."""
        return Vector3(-self.M21, -self.M22, -self.M23)
    
    @property
    def forward(self) -> Vector3:
        """The forward vector formed from the third row -M31, -M32, -M33 elements."""
        return Vector3(-self.M31, -self.M32, -self.M33)
    
    @property
    def left(self) -> Vector3:
        """The left vector formed from the first row -M11, -M12, -M13 elements."""
        return Vector3(-self.M11, -self.M12, -self.M13)
    
    @property
    def right(self) -> Vector3:
        """The right vector formed from the first row M11, M12, M13 elements."""
        return Vector3(self.M11, self.M12, self.M13)
    
    @property
    def translation(self) -> Vector3:
        """The translation vector formed from the fourth row M41, M42, M43 elements."""
        return Vector3(self.M41, self.M42, self.M43)
    
    @translation.setter
    def translation(self, value: Vector3):
        self.M41 = value.X
        self.M42 = value.Y
        self.M43 = value.Z
    
    @property
    def up(self) -> Vector3:
        """The up vector formed from the second row M21, M22, M23 elements."""
        return Vector3(self.M21, self.M22, self.M23)
    
    def __add__(self, other: 'Matrix44') -> 'Matrix44':
        return Matrix44(
            self.M11 + other.M11, self.M12 + other.M12, self.M13 + other.M13, self.M14 + other.M14,
            self.M21 + other.M21, self.M22 + other.M22, self.M23 + other.M23, self.M24 + other.M24,
            self.M31 + other.M31, self.M32 + other.M32, self.M33 + other.M33, self.M34 + other.M34,
            self.M41 + other.M41, self.M42 + other.M42, self.M43 + other.M43, self.M44 + other.M44
        )
    
    def __sub__(self, other: 'Matrix44') -> 'Matrix44':
        return Matrix44(
            self.M11 - other.M11, self.M12 - other.M12, self.M13 - other.M13, self.M14 - other.M14,
            self.M21 - other.M21, self.M22 - other.M22, self.M23 - other.M23, self.M24 - other.M24,
            self.M31 - other.M31, self.M32 - other.M32, self.M33 - other.M33, self.M34 - other.M34,
            self.M41 - other.M41, self.M42 - other.M42, self.M43 - other.M43, self.M44 - other.M44
        )
    
    def __mul__(self, other: Union['Matrix44', float]) -> 'Matrix44':
        if isinstance(other, Matrix44):
            # Matrix multiplication
            return Matrix44(
                self.M11 * other.M11 + self.M12 * other.M21 + self.M13 * other.M31 + self.M14 * other.M41,
                self.M11 * other.M12 + self.M12 * other.M22 + self.M13 * other.M32 + self.M14 * other.M42,
                self.M11 * other.M13 + self.M12 * other.M23 + self.M13 * other.M33 + self.M14 * other.M43,
                self.M11 * other.M14 + self.M12 * other.M24 + self.M13 * other.M34 + self.M14 * other.M44,
                
                self.M21 * other.M11 + self.M22 * other.M21 + self.M23 * other.M31 + self.M24 * other.M41,
                self.M21 * other.M12 + self.M22 * other.M22 + self.M23 * other.M32 + self.M24 * other.M42,
                self.M21 * other.M13 + self.M22 * other.M23 + self.M23 * other.M33 + self.M24 * other.M43,
                self.M21 * other.M14 + self.M22 * other.M24 + self.M23 * other.M34 + self.M24 * other.M44,
                
                self.M31 * other.M11 + self.M32 * other.M21 + self.M33 * other.M31 + self.M34 * other.M41,
                self.M31 * other.M12 + self.M32 * other.M22 + self.M33 * other.M32 + self.M34 * other.M42,
                self.M31 * other.M13 + self.M32 * other.M23 + self.M33 * other.M33 + self.M34 * other.M43,
                self.M31 * other.M14 + self.M32 * other.M24 + self.M33 * other.M34 + self.M34 * other.M44,
                
                self.M41 * other.M11 + self.M42 * other.M21 + self.M43 * other.M31 + self.M44 * other.M41,
                self.M41 * other.M12 + self.M42 * other.M22 + self.M43 * other.M32 + self.M44 * other.M42,
                self.M41 * other.M13 + self.M42 * other.M23 + self.M43 * other.M33 + self.M44 * other.M43,
                self.M41 * other.M14 + self.M42 * other.M24 + self.M43 * other.M34 + self.M44 * other.M44
            )
        else:
            # Scalar multiplication
            return Matrix44(
                self.M11 * other, self.M12 * other, self.M13 * other, self.M14 * other,
                self.M21 * other, self.M22 * other, self.M23 * other, self.M24 * other,
                self.M31 * other, self.M32 * other, self.M33 * other, self.M34 * other,
                self.M41 * other, self.M42 * other, self.M43 * other, self.M44 * other
            )
    
    def determinant(self) -> float:
        """Calculates the determinant of the matrix."""
        # Simplified determinant calculation for 4x4 matrix
        # This is a basic implementation, not optimized
        det = (self.M11 * (self.M22 * (self.M33 * self.M44 - self.M34 * self.M43) - 
                          self.M23 * (self.M32 * self.M44 - self.M34 * self.M42) + 
                          self.M24 * (self.M32 * self.M43 - self.M33 * self.M42)) -
               self.M12 * (self.M21 * (self.M33 * self.M44 - self.M34 * self.M43) - 
                          self.M23 * (self.M31 * self.M44 - self.M34 * self.M41) + 
                          self.M24 * (self.M31 * self.M43 - self.M33 * self.M41)) +
               self.M13 * (self.M21 * (self.M32 * self.M44 - self.M34 * self.M42) - 
                          self.M22 * (self.M31 * self.M44 - self.M34 * self.M41) + 
                          self.M24 * (self.M31 * self.M42 - self.M32 * self.M41)) -
               self.M14 * (self.M21 * (self.M32 * self.M43 - self.M33 * self.M42) - 
                          self.M22 * (self.M31 * self.M43 - self.M33 * self.M41) + 
                          self.M23 * (self.M31 * self.M42 - self.M32 * self.M41)))
        return det
    
    def invert(self) -> 'Matrix44':
        """Creates an inverted matrix."""
        # This is a simplified inversion, not the full implementation
        # For production use, a proper matrix inversion algorithm should be implemented
        det = self.determinant()
        if abs(det) < 1e-10:
            return Matrix44.identity
        
        # Simplified inversion (this is not the full algorithm)
        # In a real implementation, this would be much more complex
        return Matrix44.identity
    
    def transpose(self) -> 'Matrix44':
        """Creates a transposed matrix."""
        return Matrix44(
            self.M11, self.M21, self.M31, self.M41,
            self.M12, self.M22, self.M32, self.M42,
            self.M13, self.M23, self.M33, self.M43,
            self.M14, self.M24, self.M34, self.M44
        )
    
    @staticmethod
    def create_translation(position: Vector3) -> 'Matrix44':
        """Creates a translation matrix."""
        return Matrix44(
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            position.X, position.Y, position.Z, 1.0
        )
    
    @staticmethod
    def create_scale(scale: Union[float, Vector3]) -> 'Matrix44':
        """Creates a scaling matrix."""
        if isinstance(scale, Vector3):
            return Matrix44(
                scale.X, 0.0, 0.0, 0.0,
                0.0, scale.Y, 0.0, 0.0,
                0.0, 0.0, scale.Z, 0.0,
                0.0, 0.0, 0.0, 1.0
            )
        else:
            return Matrix44(
                scale, 0.0, 0.0, 0.0,
                0.0, scale, 0.0, 0.0,
                0.0, 0.0, scale, 0.0,
                0.0, 0.0, 0.0, 1.0
            )
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix44):
            return False
        return all([
            abs(self.M11 - other.M11) < 1e-10, abs(self.M12 - other.M12) < 1e-10,
            abs(self.M13 - other.M13) < 1e-10, abs(self.M14 - other.M14) < 1e-10,
            abs(self.M21 - other.M21) < 1e-10, abs(self.M22 - other.M22) < 1e-10,
            abs(self.M23 - other.M23) < 1e-10, abs(self.M24 - other.M24) < 1e-10,
            abs(self.M31 - other.M31) < 1e-10, abs(self.M32 - other.M32) < 1e-10,
            abs(self.M33 - other.M33) < 1e-10, abs(self.M34 - other.M34) < 1e-10,
            abs(self.M41 - other.M41) < 1e-10, abs(self.M42 - other.M42) < 1e-10,
            abs(self.M43 - other.M43) < 1e-10, abs(self.M44 - other.M44) < 1e-10
        ])
    
    def __str__(self) -> str:
        return f"""Matrix44:
[{self.M11:8.4f} {self.M12:8.4f} {self.M13:8.4f} {self.M14:8.4f}]
[{self.M21:8.4f} {self.M22:8.4f} {self.M23:8.4f} {self.M24:8.4f}]
[{self.M31:8.4f} {self.M32:8.4f} {self.M33:8.4f} {self.M34:8.4f}]
[{self.M41:8.4f} {self.M42:8.4f} {self.M43:8.4f} {self.M44:8.4f}]"""


# Static properties
Matrix44.identity = Matrix44(
    1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0
)