from enum import Enum

class CounterType(Enum):
    """** NOTE: ADDED in CFX 1.3 **
    An enumeration indicating the type of counter that is capture by the Endpoint and its resources / sensors"""
    
    # Unknown counter
    Unkwnown = "Unkwnown"
    # General counter
    General = "General"
    # Non standard counter.
    # It shall be used in combination with the CustomCounterType field
    NonStandard = "NonStandard"
    # Rotation, mileage measured by a sensor
    Odometer = "Odometer"
    # Time based sensor, in hour
    Timer = "Timer"
    # Counter for the sensor specified by the name and position
    # It can be, among the others: cuts, flashes, pumps, picking components, placed components, rotations
    ActivityCount = "ActivityCount"