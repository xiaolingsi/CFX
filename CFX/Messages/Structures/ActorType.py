"""
Types of Operators
"""

from enum import Enum


class ActorType(Enum):
    """
    Types of Operators
    """
    
    # A human being is performing the operation
    Human = "Human"
    
    # A robotic / automated device is performing the operation
    Robot = "Robot"
    
    # A remote system or artificial intelligence entity is performing the operation
    RemoteSystem = "RemoteSystem"