from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import datetime

@dataclass_json
@dataclass
class ErrorInformation:
    """** NOTE: ADDED in CFX 1.3 **
    Dynamic structure that contains information related to the errors of the 
    resources / sub-resources in an Endpoint.
    It is used in maintenance context"""
    
    # Name of the error(text output)
    Name: Optional[str] = None
    
    # When available, the error code from the machine
    ErrorCode: Optional[int] = None
    
    # The time when the error has been raised
    OccurrenceTime: Optional[datetime] = None