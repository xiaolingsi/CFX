from enum import Enum


class WorkOrderStatus(Enum):
    """
    Indicates the current status of a Work Order
    """
    
    # The Work Order has not yet been approved, and may not be scheduled or executed.
    AwaitingApproval = "AwaitingApproval"
    
    # THe Work Order has been approved, and is available to be scheduled or executed.
    ApprovedAndPending = "ApprovedAndPending"
    
    # THe Work Order has been scheduled for production, but is not yet executing.
    Scheduled = "Scheduled"
    
    # The Work Order is currently being executed, and is in process.
    InProcess = "InProcess"
    
    # The Work Order has been completed.
    Completed = "Completed"
    
    # The Work Order has been closed.
    Closed = "Closed"
    
    # The Work Order has been placed on hold.  No work should occur on this order at this time.
    OnHold = "OnHold"
    
    # The Work Order has been cancelled.  
    Cancelled = "Cancelled"