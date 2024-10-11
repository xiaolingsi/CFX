from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ValidationResult import ValidationResult
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


