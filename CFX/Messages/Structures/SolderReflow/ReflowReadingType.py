"""
Reflow Reading Type enumeration
"""

from enum import Enum


class ReflowReadingType(Enum):
    """
    An enumeration indicating the type of a setpoint within a particular area of a reflow zone.
    """
    
    # The reading a temperature reading, expressed in degrees celcius (C).
    Temperature = "Temperature"
    
    # The reading is an oxygen reading, expressed in parts per million (PPM).
    O2 = "O2"
    
    # The reading is an power reading, expressed in watts (w).
    Power = "Power"
    
    # The reading is an power level reading, expressed as a percentage from 0.0 to 100.0 (%).
    PowerLevel = "PowerLevel"
    
    # The reading is a vacuum reading, expressed in Pascals (Pa).
    Vacuum = "Vacuum"
    
    # The reading is a vacuum reading, expressed in seconds (s).
    VacuumHoldTime = "VacuumHoldTime"
    
    # A measure of the amount of relative convection, expressed in Pascals (Pa).
    ConvectionRate = "ConvectionRate"