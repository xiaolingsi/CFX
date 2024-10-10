from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.UnitPojo.UnitPosition import UnitPosition


@dataclass_json
@dataclass
class ValidateUnitsRequest(CFXMessage):
    HermesIdentifier:str
    Lane:int
    PrimaryIdentifier:str
    Units:list
    Validations:list

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, primaryIdentifier = "", units=None):
        super().__init__()
        if units is None:
            units = []
        self.type = "CFX.InformationSystem.UnitValidation.ValidateUnitsRequest,CFX"
        self.message_name = "CFX.InformationSystem.UnitValidation.ValidateUnitsRequest"
        self.HermesIdentifier = ""
        self.Lane = 0
        self.PrimaryIdentifier = primaryIdentifier
        self.Units = units
        self.Validations = []


if __name__ == '__main__':
    units = []
    units.append(UnitPosition())
    validateUnitsRequest = ValidateUnitsRequest(primaryIdentifier="aaa",units = units)
    print(validateUnitsRequest.to_cfx_json())