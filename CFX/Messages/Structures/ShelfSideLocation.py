from enum import Enum


class ShelfSideLocation(Enum):
    """
    ** NOTE: ADDED in CFX 1.7 **
    A Shelf side location
    """
    
    # Unknown shelf side location
    Unknown = "Unknown"
    
    # Front side of the shelf
    Front = "Front"
    
    # Back side of the shelf
    Back = "Back"