from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition
from CFX.Messages.Structures.ValidationType import ValidationType


@dataclass_json
@dataclass
class ValidateUnitsRequest(CFXMessage):
    Validations: List[ValidationType]
    PrimaryIdentifier: str
    HermesIdentifier: str
    Units: List[UnitPosition]
    Lane: int

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, primary_identifier: str = "", hermes_identifier: str = "", 
                 units: List[UnitPosition] = None, validations: List[ValidationType] = None, lane: int = None):
        super().__init__()
        self.type = "CFX.InformationSystem.UnitValidation.ValidateUnitsRequest,CFX"
        self.message_name = "CFX.InformationSystem.UnitValidation.ValidateUnitsRequest"
        self.Validations = validations or []
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.Units = units or []
        self.Lane = lane
