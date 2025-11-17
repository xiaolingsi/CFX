from enum import Enum


class WorkResult(Enum):
    """
    The result of an operation where work was performed on a production unit
    """
    
    # The work was completed successfully
    Completed = "Completed"
    
    # The work was completed, but with an undesireable result
    Failed = "Failed"
    
    # Work was not completed
    Aborted = "Aborted"
    
    # ** NOTE: ADDED in CFX 1.4 **
    # The test was skipped because of (virtual) bad mark
    Skipped = "Skipped"