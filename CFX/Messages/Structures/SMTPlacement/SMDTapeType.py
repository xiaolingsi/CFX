"""
Tape type for Package of Taped SMD's
"""

from enum import Enum


class SMDTapeType(Enum):
    """
    Tape type for Package of Taped SMD's
    """
    
    # Embossed Tape
    Embossed = "Embossed"
    
    # Punched Paper Tape
    PunchedPaper = "PunchedPaper"