from enum import Enum

class MSDState(Enum):
    """Possible states of packages of moisture sensitive devices"""
    
    # Unspecified state
    Unspecified = "Unspecified"
    # Sealed and never opened.
    NeverOpened = "NeverOpened"
    # Open and exposed to the atmosphere
    Exposed = "Exposed"
    # Open but stored in low humidity environment
    InDryStorage = "InDryStorage"
    # Exposed to atmosphere/moisture beyond acceptable limits.
    Expired = "Expired"