from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class UnitsArrived(CFXMessage):
    def to_cfx_json(self):
        return self.to_json()

    # type: str
    # message_name: str
    PrimaryIdentifier: str
    HermesIdentifier: str
    UnitCount: int
    Lane: int
    Units: list

    def __init__(self, primaryIdentifier="", hermesIdentifier="", Lane=0):
        super().__init__()
        self.type = "CFX.Production.UnitsArrived,CFX"
        self.message_name = "CFX.Production.UnitsArrived"
        self.PrimaryIdentifier = primaryIdentifier
        self.HermesIdentifier = hermesIdentifier
        self.Lane = Lane
        self.Units = list()
        self.UnitCount = 0

    def add_units(self, unit: UnitPosition):
        self.Units.append(unit)
        self.UnitCount += 1


