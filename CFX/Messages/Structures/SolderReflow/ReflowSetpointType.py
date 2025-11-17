"""
Reflow Setpoint Type enumeration
"""

from enum import Enum


class ReflowSetpointType(Enum):
    """
    An enumeration indicating the type of a setpoint within a particular area of a reflow zone.
    """
    
    # The setpoint is a temperature setpoint, expressed in degrees celcius (C).
    Temperature = "Temperature"
    
    # The setpoint is an oxygen setpoint, expressed in parts per million (PPM).
    O2 = "O2"
    
    # The setpoint is a vacuum setpoint, expressed in Pascals (Pa).
    Vacuum = "Vacuum"
    
    # The setpoint is a vacuum setpoint, expressed in seconds (s).
    VacuumHoldTime = "VacuumHoldTime"