"""
Reflow Zone Type enumeration
"""

from enum import Enum


class ReflowZoneType(Enum):
    """
    An enumeration indicating the nature of a zone within a reflow oven
    """
    
    # This is a pre-heat zone.
    PreHeat = "PreHeat"
    
    # The zone is a thermal soak zone.
    Soak = "Soak"
    
    # This zone is intended to induce solder reflow.
    Reflow = "Reflow"
    
    # This is a cooling zone.
    Cool = "Cool"