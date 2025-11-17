import uuid
from datetime import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier
from CFX.Messages.Structures.WorkOrderActionType import WorkOrderActionType
from CFX.Messages.Structures.WorkOrderActionState import WorkOrderActionState
from CFX.Messages.Structures.Surface import Surface


@dataclass_json
@dataclass
class WorkOrderActionExecuted(CFXMessage):
    WorkOrderActionInstanceId: uuid.UUID
    WorkOrderIdentifier: WorkOrderIdentifier
    TimeStamp: datetime
    Type: WorkOrderActionType
    State: WorkOrderActionState
    Comments: str
    RelevantSurface: Surface
    RecipeName: str
    RecipeRevision: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, work_order_identifier: WorkOrderIdentifier = None, time_stamp: datetime = None, 
                 type: WorkOrderActionType = WorkOrderActionType.Uncategorized, 
                 state: WorkOrderActionState = WorkOrderActionState.Completed, comments: str = "", 
                 relevant_surface: Surface = None, recipe_name: str = "", recipe_revision: str = ""):
        super().__init__()
        self.type = "CFX.Production.WorkOrderActionExecuted,CFX"
        self.message_name = "CFX.Production.WorkOrderActionExecuted"
        self.WorkOrderActionInstanceId = uuid.uuid4()
        self.WorkOrderIdentifier = work_order_identifier or WorkOrderIdentifier()
        self.TimeStamp = time_stamp or CFXUtils.get_iso8601_time()
        self.Type = type
        self.State = state
        self.Comments = comments
        self.RelevantSurface = relevant_surface or Surface.Unspecified
        self.RecipeName = recipe_name
        self.RecipeRevision = recipe_revision