from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .StatusResult import StatusResult

@dataclass_json
@dataclass
class RequestResult:
    """A structure which indicates whether or not a CFX request to an endpoint was successful.
    If not successful, information about the nature of the failure is provided."""
    
    # An enumeration indication whether or not the request was successfully executed
    Result: Optional[StatusResult] = StatusResult.Success
    
    # In the case of a failure, an integer-based, endpoint-specific error code
    # indicating the nature of the failure
    ResultCode: int = 0
    
    # In the case of a failure, a human readable message indicating the nature of the failure
    Message: Optional[str] = None