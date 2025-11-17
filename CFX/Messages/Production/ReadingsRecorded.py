import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Reading import Reading


@dataclass_json
@dataclass
class ReadingsRecorded(CFXMessage):
    TransactionId: uuid.UUID
    Readings: List[Reading]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, readings: List[Reading] = None):
        super().__init__()
        self.type = "CFX.Production.ReadingsRecorded,CFX"
        self.message_name = "CFX.Production.ReadingsRecorded"
        self.TransactionId = transaction_id
        self.Readings = readings or []