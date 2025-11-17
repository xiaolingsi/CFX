from enum import Enum


class WorkOrderActionState(Enum):
    """
    ** NOTE: ADDED in CFX 1.2 **
    Describes the state of a work order action.
    """
    
    # The work order action has started, but is not yet complete.
    Started = "Started"
    
    # The work order action was aborted.
    Aborted = "Aborted"
    
    # The work order action successfullly completed.
    Completed = "Completed"