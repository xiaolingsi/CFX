from enum import Enum


class ComponentElectricalTestUnit(Enum):
    """
    Unit used for an electrical test
    """
    
    Unknown = "Unknown"
    Ohm = "Ohm"
    Farad = "Farad"
    Henry = "Henry"
    Volt = "Volt"
    Hertz = "Hertz"
    Watt = "Watt"