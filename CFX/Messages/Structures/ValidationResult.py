from dataclasses import dataclass

from dataclasses_json import dataclass_json

from CFX.Messages.Structures.ValidationStatus import ValidationStatus


@dataclass_json
@dataclass
class ValidationResult(object):
    FailureCode: int
    Message: str
    PositionNumber: int
    Result: ValidationStatus
    UniqueIdentifier: str


    def __init__(self,failureCode = 0,message = "",positionNumber = 0,result = ValidationStatus.Passed,uniqueIdentifier = ""):
        self.FailureCode = failureCode
        self.Message = message
        self.PositionNumber = positionNumber
        self.Result = result
        self.UniqueIdentifier = uniqueIdentifier


