from enum import Enum

class MaintenanceType(Enum):
    """Types of Maintenance"""
    
    # Maintenance intended to prevent breakdowns that have not yet occurred
    Preventive = "Preventive"
    # Inspection intended to prevent breakdowns that have not yet occurred
    Inspection = "Inspection"
    # Repair of a breakdown that has occurred.
    Repair = "Repair"
    # Testing of repairs made
    Test = "Test"