import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Tool import Tool
from CFX.Messages.Structures.Cleaning.CleaningStep import CleaningStep


@dataclass_json
@dataclass
class ToolsCleaned(CFXMessage):
    TransactionID: uuid.UUID
    Tools: List[Tool]
    CleaningSteps: List[CleaningStep]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: uuid.UUID = None, tools: List[Tool] = None, cleaning_steps: List[CleaningStep] = None):
        super().__init__()
        self.type = "CFX.Production.ToolsCleaned,CFX"
        self.message_name = "CFX.Production.ToolsCleaned"
        self.TransactionID = transaction_id or uuid.uuid4()
        self.Tools = tools or []
        self.CleaningSteps = cleaning_steps or []