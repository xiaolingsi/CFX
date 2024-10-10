import uuid
from dataclasses import dataclass

from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ProcessingResult import ProcessingResult


@dataclass_json
@dataclass
class UnitsProcessed(CFXMessage):
    # CommonProcessData: ProcessData
    OverallResult: ProcessingResult
    TransactionId: uuid.uuid4
    UnitProcessData: list

    def to_cfx_json(self):
        pass

    def __init__(self):
        super().__init__()
        raise Exception("Not Finished")
        self.type = "CFX.Production.Processing.UnitsProcessed,CFX"
        self.message_name = "CFX.Production.Processing.UnitsProcessed"
