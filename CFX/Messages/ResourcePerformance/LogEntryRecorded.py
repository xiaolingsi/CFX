from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.LogImportance import LogImportance
from CFX.Messages.Structures.Stage import Stage


@dataclass_json
@dataclass
class LogEntryRecorded(CFXMessage):
    Importance: LogImportance = field(default_factory=lambda: LogImportance.Information)
    InformationId: str = ""
    Lane: Optional[int] = None
    Message: str = ""
    Stage: Optional[Stage] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, information_id="", message="", importance=None, lane=None, stage=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.LogEntryRecorded,CFX"
        self.message_name = "CFX.ResourcePerformance.LogEntryRecorded"
        self.Importance = importance if importance is not None else LogImportance.Information
        self.InformationId = information_id
        self.Lane = lane
        self.Message = message
        self.Stage = stage


