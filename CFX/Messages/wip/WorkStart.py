import uuid

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class WorkStarted(CFXMessage):

    def to_cfx_json(self):
        return self.to_json()

    TransactionID: uuid.uuid4()
    PrimaryIdentifier: str
    HermesIdentifier: str
    Units: list
    Lane:int

    def __init__(self, transctionID=uuid.uuid4(),  primaryIdentifier="",hermesIdentifier="",lane:int = 0):
        super().__init__()
        self.type = "CFX.Production.WorkStarted,CFX"
        self.message_name = "CFX.Production.WorkStarted"
        self.TransactionID = transctionID
        self.PrimaryIdentifier = primaryIdentifier
        self.HermesIdentifier = hermesIdentifier
        self.Units = list()
        self.UnitCount = 0
        self.Lane = lane

    def add_unit(self, unit: UnitPosition):
        self.Units.append(unit)
        self.UnitCount += 1


if __name__ == '__main__':
    workStarted = WorkStarted(primaryIdentifier="AAA",hermesIdentifier="BBB")
    workStarted.add_unit(UnitPosition("a", 2, "A", 1.1, 2.1, 0.5, True, False))
    print(workStarted.to_cfx_json())