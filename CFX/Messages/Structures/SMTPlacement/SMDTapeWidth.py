"""
Width of Taped SMD's
"""

from enum import Enum


class SMDTapeWidth(Enum):
    """
    Width of Taped SMD's
    """
    
    # 8mm Width
    Tape8mm = "Tape8mm"
    
    # 12mm Width
    Tape12mm = "Tape12mm"
    
    # 16mm Width
    Tape16mm = "Tape16mm"
    
    # 24mm Width
    Tape24mm = "Tape24mm"
    
    # 32mm Width
    Tape32mm = "Tape32mm"
    
    # 44mm Width
    Tape44mm = "Tape44mm"
    
    # 79mm Width
    Tape79mm = "Tape79mm"
    
    # Some width other than those specified in this enumeration
    Other = "Other"