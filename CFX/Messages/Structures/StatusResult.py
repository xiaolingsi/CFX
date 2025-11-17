"""
Result of an operation
"""

from enum import Enum


class StatusResult(Enum):
    """
    Result of an operation
    """
    
    # Successful completion of operation
    Success = "Success"
    
    # A portion of the request completed successfully (another portion did not).
    # Where applicable, the response message will contain details on the portion that did 
    # not succeed.
    PartialSuccess = "PartialSuccess"
    
    # Operation was not completed successfully
    Failed = "Failed"
    
    # Operation successful but with warning(s)
    Warning = "Warning"