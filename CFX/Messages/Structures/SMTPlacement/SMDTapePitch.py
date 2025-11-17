"""
Pitch of Tape Feeder
"""

from enum import Enum


class SMDTapePitch(Enum):
    """
    Pitch of Tape Feeder
    """
    
    # Adjustable Pitch Feeder
    Adjustable = "Adjustable"
    
    # 2mm Pitch
    Pitch2mm = "Pitch2mm"
    
    # 4mm Pitch
    Pitch4mm = "Pitch4mm"
    
    # 8mm Pitch
    Pitch8mm = "Pitch8mm"
    
    # 12mm Pitch
    Pitch12mm = "Pitch12mm"
    
    # 16mm Pitch
    Pitch16mm = "Pitch16mm"
    
    # 24mm Pitch
    Pitch24mm = "Pitch24mm"
    
    # 32mm Pitch
    Pitch32mm = "Pitch32mm"
    
    # 36mm Pitch
    Pitch36mm = "Pitch36mm"
    
    # Pitch other than those specified in this enumeration
    Other = "Other"