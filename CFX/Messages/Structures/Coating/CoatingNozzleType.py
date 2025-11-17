from enum import Enum


class CoatingNozzleType(Enum):
    """
    An enumeration indicating the nature of a Nozzle within a Coating Machine
    NOTE: ADDED in CFX 1.5
    """
    
    # This is a Jetter Nozzle.
    Jetter = "Jetter"
    
    # The is a Dispensing Nozzle.
    Dispensing = "Dispensing"
    
    # The is a Type of Film Coater.
    Curtain = "Curtain"
    
    # The is a Type of Film Coater.
    Spray = "Spray"
    
    # The is a Type of Film Coater.
    Doser = "Doser"