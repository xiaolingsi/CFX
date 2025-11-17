from enum import Enum


class CleaningStepType(Enum):
    """
    An enumeration indicating the type of cleaning step
    NOTE: ADDED in CFX 1.5
    """
    
    # Cleaning step pre-wash
    PreWash = "PreWash"
    
    # Cleaning step wash
    Wash = "Wash"
    
    # Cleaning step pre-rinse
    PreRinse = "PreRinse"
    
    # Cleaning step rinse
    Rinse = "Rinse"
    
    # Cleaning step final rinse
    FinalRinse = "FinalRinse"
    
    # Cleaning step dry
    Dry = "Dry"