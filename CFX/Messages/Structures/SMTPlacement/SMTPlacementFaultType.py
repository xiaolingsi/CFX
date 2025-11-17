"""
Types of SMT Placement Faults
"""

from enum import Enum


class SMTPlacementFaultType(Enum):
    """
    Types of SMT Placement Faults
    """
    
    # Insufficient vacuum to manipulate part.
    VacuumError = "VacuumError"
    
    # Problem with the x motion axis
    XAxisError = "XAxisError"
    
    # Problem with the y motion axis
    YAxisError = "YAxisError"
    
    # Problem with the z motion axis
    ZAxisError = "ZAxisError"
    
    # Part not recognized by vision system
    RecognitionError = "RecognitionError"
    
    # Part not picked up properly
    PickupError = "PickupError"
    
    # Part not place properly
    PlacementError = "PlacementError"
    
    # Insufficient or incorrect lighting. Vision system not able to characterize part
    LightingError = "LightingError"
    
    # Error with placement head
    HeadError = "HeadError"
    
    # Error with placement nozzle
    NozzleError = "NozzleError"
    
    # Component dropped in transit
    ComponentDropped = "ComponentDropped"
    
    # Material supply exhausted
    PartsExhaust = "PartsExhaust"
    
    # Error decoding fiducial reference mark
    FiducialError = "FiducialError"
    
    # Material supply partially exhausted. Can happen if a head is supposed to pickup in several locations and one of them is exhausted
    # ** NOTE: ADDED in CFX 1.5 **
    PartsPartiallyExhaust = "PartsPartiallyExhaust"
    
    # Material supply will soon be exhausted
    # ** NOTE: ADDED in CFX 1.5 **
    LowQuantity = "LowQuantity"
    
    # Error with placement feeder
    # ** NOTE: ADDED in CFX 1.5 **
    FeederError = "FeederError"