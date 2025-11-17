from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import datetime
from ..OperationStatus import OperationStatus
from .VerificationType import VerificationType

@dataclass_json
@dataclass
class VerificationInformation:
    """** NOTE: ADDED in CFX 1.3 **
    Dynamic structure that contains information related to the verification of the 
    resources / sub-resources in an Endpoint.
    It may be used to model the verification results on  
    parts that may require traceable operations (i.e. maintenance)"""
    
    # Name of the verification
    Name: Optional[str] = None
    
    # The status of the performed verification.
    Status: Optional[OperationStatus] = None
    
    # The value of the performed verification.
    Value: Optional[float] = None
    
    # The unit of measure of the performed verification (if applicable)
    UnitOfMeasure: Optional[str] = None
    
    # The location of the data source providing the verification information (optional, only if available).
    # It may be used to distinguish, for example, the type and location of the part: head, camera, nozzle
    # Where applicable, a dot (".") notation should be utilized to designate specific positions.
    # Examples: MODULE1.BEAM1.HEADPOS2, MODULE1.NEST3.NOZZLESLOT4, etc.
    VerificationLocation: Optional[str] = None
    
    # The type of the verification that is performed on this resource / machine.
    Type: Optional[VerificationType] = None
    
    # If the verification is valid or should be ignored bay the receiving system. Default (i.e. null) = true
    IsValid: Optional[bool] = None
    
    # The last time when the verification has been executed
    LastExecution: Optional[datetime] = None
    
    # Free text for additional comment on the performed verification, if required
    Comment: Optional[str] = None