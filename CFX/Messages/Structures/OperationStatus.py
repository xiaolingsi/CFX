from enum import Enum

class OperationStatus(Enum):
    """Status of a performed operation, for example Calibration"""
    
    # Status of the operation is not known
    Unknown = "Unknown"
    # The operation failed
    Failed = "Failed"
    # The operation was succesfull 
    Ok = "Ok"