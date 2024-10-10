import uuid

from CFX.CFXMessage import CFXMessage
from CFX.Messages.UnitPojo.UnitPosition import UnitPosition
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.WorkResult import WorkResult


@dataclass_json
@dataclass
class WorkCompleted(CFXMessage):

    def to_cfx_json(self):
        return self.to_json()

    TransactionID: uuid.uuid4()
    Result: WorkResult
    PrimaryIdentifier: str
    HermesIdentifier: str
    Units: list

    def __init__(self, transctionID=uuid.uuid4(), Result: WorkResult = WorkResult.Completed, primaryIdentifier="",
                 hermesIdentifier=""):
        super().__init__()
        self.type = "CFX.Production.WorkCompleted,CFX"
        self.message_name = "CFX.Production.WorkCompleted"
        self.TransactionID = transctionID
        self.PrimaryIdentifier = primaryIdentifier
        self.Result = Result
        self.HermesIdentifier = hermesIdentifier
        self.Units = list()
        self.UnitCount = 0

    def add_unit(self, unit: UnitPosition):
        self.Units.append(unit)
        self.UnitCount += 1


if __name__ == '__main__':
    workCompleted = WorkCompleted(Result=WorkResult.Failed,primaryIdentifier="AA",hermesIdentifier="BB")
    workCompleted.add_unit(UnitPosition("a", 2, "A", 1.1, 2.1, 0.5, True, False))
    print(workCompleted.to_cfx_json())