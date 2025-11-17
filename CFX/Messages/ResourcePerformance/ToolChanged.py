from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Tool import Tool
from CFX.Messages.Structures.ToolHolder import ToolHolder


@dataclass_json
@dataclass
class ToolChanged(CFXMessage):
    """
    Sent when a new tool is selected for active use at a production endpoint.
    """
    OldTool: Optional[Tool] = None
    ReturnedToHolder: Optional[ToolHolder] = None
    NewTool: Optional[Tool] = None
    LoadedFromHolder: Optional[ToolHolder] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, OldTool=None, ReturnedToHolder=None, NewTool=None, LoadedFromHolder=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.ToolChanged,CFX"
        self.message_name = "CFX.ResourcePerformance.ToolChanged"
        self.OldTool = OldTool
        self.ReturnedToHolder = ReturnedToHolder
        self.NewTool = NewTool
        self.LoadedFromHolder = LoadedFromHolder