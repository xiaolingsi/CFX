from enum import Enum

class VerificationType(Enum):
    """** NOTE: ADDED in CFX 1.3 **
    An enumeration indicating the type of verification that can be executed during the process (i.e. maintenance)"""
    
    # Unknown verification type
    Unkwnown = "Unkwnown"
    # General verification of the machine
    General = "General"
    # Special verification, specific for a given part
    Special = "Special"