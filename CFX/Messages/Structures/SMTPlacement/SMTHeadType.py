"""
An enumeration indicating different types of SMT heads that might exist at an endpoint.
"""

from enum import Enum


class SMTHeadType(Enum):
    """
    An enumeration indicating different types of SMT heads that might exist at an endpoint.
    """
    
    # Turret head type
    Turret = "Turret"
    
    # Pulsar head type
    Pulsar = "Pulsar"