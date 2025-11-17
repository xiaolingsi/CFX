from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ValidationResult import ValidationResult
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class ValidateUnitsResponse(CFXMessage):
    Result: RequestResult
    PrimaryResult: ValidationResult
    ValidationResults: List[ValidationResult]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, primary_result: ValidationResult = None, 
                 validation_results: List[ValidationResult] = None):
        super().__init__()
        self.type = "CFX.InformationSystem.UnitValidation.ValidateUnitsResponse,CFX"
        self.message_name = "CFX.InformationSystem.UnitValidation.ValidateUnitsResponse"
        self.Result = result or RequestResult()
        self.PrimaryResult = primary_result or ValidationResult()
        self.ValidationResults = validation_results or []


