"""
Reflow Sub-Zone Type enumeration
"""

from enum import Enum


class ReflowSubZoneType(Enum):
    """
    An enumeration indicating an area within a reflow zone that is under thermal control.
    """
    
    # Applies to the entire zone.
    WholeZone = "WholeZone"
    
    # Applies to the region of the zone above the printed circuit card.
    Top = "Top"
    
    # Applies to the region of the zone below the printed circuit card.
    Bottom = "Bottom"