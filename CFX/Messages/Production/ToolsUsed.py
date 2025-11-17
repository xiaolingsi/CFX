import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ToolUsed import ToolUsed


@dataclass_json
@dataclass
class ToolsUsed(CFXMessage):
    TransactionId: uuid.UUID
    UsedTools: List[ToolUsed]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, used_tools: List[ToolUsed] = None):
        super().__init__()
        self.type = "CFX.Production.ToolsUsed,CFX"
        self.message_name = "CFX.Production.ToolsUsed"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.UsedTools = used_tools or []