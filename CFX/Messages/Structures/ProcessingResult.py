from enum import Enum

class ProcessingResult(Enum):
    """The overall result of processing performed on a production unit in the course of production."""
    
    # The processing succeeded
    Succeeded = "Succeeded"
    # The processing failed
    Failed = "Failed"
    # The processing could not be completed because an error occurred.
    Error = "Error"
    # The processing was aborted by the operator / user.
    Aborted = "Aborted"
    # ** NOTE: ADDED in CFX 1.4 **
    # The test was skipped because of (virtual) bad mark
    Skipped = "Skipped"