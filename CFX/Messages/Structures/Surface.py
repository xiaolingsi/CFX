from enum import Enum


class Surface(Enum):
    """
    ** NOTE: ADDED in CFX 1.3 **
    For use two-dimensional production (as in the case of PCBA production).  Identifies the surface of the unit
    under production (product) that is relevant for a given process or situation.
    """
    
    # The relevant surface has not been specified
    Unspecified = "Unspecified"
    
    # The primary surface of the product is relevant
    PrimarySurface = "PrimarySurface"
    
    # The secondary surface is relevant
    SecondarySurface = "SecondarySurface"