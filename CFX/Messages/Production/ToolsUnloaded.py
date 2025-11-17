import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Tool import Tool


@dataclass_json
@dataclass
class ToolsUnloaded(CFXMessage):
    TransactionID: uuid.UUID
    Tools: List[Tool]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, tools: List[Tool] = None):
        super().__init__()
        self.type = "CFX.Production.ToolsUnloaded,CFX"
        self.message_name = "CFX.Production.ToolsUnloaded"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.Tools = tools or []