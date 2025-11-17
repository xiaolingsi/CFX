from enum import Enum


class InspectionMethod(Enum):
    """
    Method of testing
    """
    
    # The inspection was performed by a human being
    Human = "Human"
    
    # The inspection was performed by automated optical inspection equipment / device
    AOI = "AOI"
    
    # The inspection was performed by automated solder paste inspection equipment / device
    SPI = "SPI"
    
    # The test was performed by an automated X-Ray inspection machine
    AXI = "AXI"