from enum import Enum

class MSDLevel(Enum):
    """Levels of Moisture Sensitivity (for electronic devices)"""
    
    # Unknown sensitivity
    Unspecified = "Unspecified"
    # Sensitivity Level 1
    MSL1 = "MSL1"
    # Sensitivity Level 2
    MSL2 = "MSL2"
    # Sensitivity Level 2A
    MSL2A = "MSL2A"
    # Sensitivity Level 3
    MSL3 = "MSL3"
    # Sensitivity Level 4
    MSL4 = "MSL4"
    # Sensitivity Level 5
    MSL5 = "MSL5"
    # Sensitivity Level 5A
    MSL5A = "MSL5A"
    # Sensitivity Level 6
    MSL6 = "MSL6"