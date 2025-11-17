from enum import Enum

class RepairResult(Enum):
    """** NOTE: ADDED in CFX 1.4 **
    The result of a repair"""
    
    # The repair was performed successfully
    RepairSuccessful = "RepairSuccessful"
    # The repair was not able to be completed
    UnableToRepair = "UnableToRepair"
    # It is not possible to repair the unit, and the unit must be scrapped
    Scrap = "Scrap"
    # The repair could not be completed because an error occurred
    Error = "Error"
    # The repair was aborted by the operator / user
    Aborted = "Aborted"