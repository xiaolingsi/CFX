"""
An enumeration indicating different types of placement for an SMT machine
"""

from enum import Enum


class SMTPlacementType(Enum):
    """
    An enumeration indicating different types of placement for an SMT machine
    """
    
    # Manual placement
    Manual = "Manual"
    
    # Step by step placement
    StepByStep = "StepByStep"
    
    # Automatic placement
    Automatic = "Automatic"