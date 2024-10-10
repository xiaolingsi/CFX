from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ValidationResult import ValidationResult
from CFX.Messages.UnitPojo.UnitPosition import UnitPosition
from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StatusResult import StatusResult


@dataclass_json
@dataclass
class ValidateUnitsResponse(CFXMessage):
    PrimaryResult: ValidationResult
    Result: RequestResult
    ValidationResults: list

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, request_result, validationResult):
        super().__init__()
        self.type = "CFX.InformationSystem.UnitValidation.ValidateUnitsResponse,CFX"
        self.message_name = "CFX.InformationSystem.UnitValidation.ValidateUnitsResponse"
        self.ValidationResults = []
        self.Result = request_result
        self.PrimaryResult = validationResult


if __name__ == '__main__':
    request_result = RequestResult(StatusResult.Success, 0, "Success")
    validationResult = ValidationResult()
    validateUnitsResponse = ValidateUnitsResponse(request_result=request_result, validationResult = validationResult)
    print(validateUnitsResponse.to_cfx_json())
