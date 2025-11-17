"""
** NOTE: ADDED in CFX 1.5 **
The status condition of a Unit.
"""

from enum import Enum


class UnitStatus(Enum):
    """
    ** NOTE: ADDED in CFX 1.5 **
    The status condition of a Unit.
    """
    
    # The production unit has completed all prior operations without defects, or with all defects resolved
    Pass = "Pass"
    
    # The production unit has not passed the preceding operation, though may be recoverable
    Fail = "Fail"
    
    # The production unit has not passed the preceding operation, and has been deemed unrepairable
    Scrap = "Scrap"
    
    # ** NOTE: ADDED in CFX 1.6 **
    # The production unit does not require processing
    Skip = "Skip"