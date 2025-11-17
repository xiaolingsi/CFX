from enum import Enum


class CleaningState(Enum):
    """
    Cleaning states (e.g., used by stencil, squeegee)
    NOTE: ADDED in CFX 1.5
    """
    
    # Unknown cleaning status
    Unknown = "Unknown"
    
    # Tool cleaned
    Cleaned = "Cleaned"
    
    # Tool not cleaned
    NotCleaned = "NotCleaned"