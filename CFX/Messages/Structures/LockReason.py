from enum import Enum


class LockReason(Enum):
    """
    Reason for a production lock condition
    """
    
    QualityIssue = "QualityIssue"
    PreventativeMaintenance = "PreventativeMaintenance"
    UnscheduledMaintenance = "UnscheduledMaintenance"
    GeneralLock = "GeneralLock"