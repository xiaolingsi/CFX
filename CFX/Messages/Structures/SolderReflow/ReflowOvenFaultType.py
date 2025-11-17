"""
An enumeration that defines the different types of faults that might occur on a solder reflow oven.
"""

from enum import Enum


class ReflowOvenFaultType(Enum):
    """
    An enumeration that defines the different types of faults that might occur on a solder reflow oven.
    """
    
    # The conveyor is moving too slowly. 
    LowBeltSpeed = "LowBeltSpeed"
    
    # The conveyor is moving too quickly.
    HighBeltSpeed = "HighBeltSpeed"