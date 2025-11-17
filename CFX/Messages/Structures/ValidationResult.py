from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ValidationStatus import ValidationStatus


@dataclass_json
@dataclass
class ValidationResult:
    """
    Indicates result of a validation that was performed on a given production unit 
    (typically by a line or factory level control system)
    """
    UniqueIdentifier: str
    PositionNumber: int
    Result: ValidationStatus
    FailureCode: int
    Message: str

    def __init__(self, unique_identifier: str = "", position_number: int = 0, 
                 result: ValidationStatus = None, failure_code: int = 0, message: str = ""):
        """
        Default constructor
        """
        self.UniqueIdentifier = unique_identifier
        self.PositionNumber = position_number
        self.Result = result or ValidationStatus.Passed
        self.FailureCode = failure_code
        self.Message = message


