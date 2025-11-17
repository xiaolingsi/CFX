from enum import Enum


class ValueAddType(Enum):
    """
    An enumeration describing the value-add nature of an activity or process.
    """
    
    RealValueAdd = "RealValueAdd"
    BusinessValueAdd = "BusinessValueAdd"
    NonValueAdd = "NonValueAdd"