from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
import uuid
from datetime import datetime
from CFX.Messages.Structures.ActivityState import ActivityState
from CFX.Messages.Structures.ValueAddType import ValueAddType


@dataclass_json
@dataclass
class Activity(object):
    """
    Dynamic structure base class. Describes an activity that was performed in the course of processing one or more
    production units. Different endpoints may produce more specific structures derived from this generic Activity structure.
    """
    
    TimeStamp: datetime
    ActivityInstanceId: uuid.UUID
    ActivityState: ActivityState
    ActivityName: Optional[str] = None
    Comments: Optional[str] = None
    ValueAddType: Optional[ValueAddType] = None

    def __init__(self, time_stamp=None, activity_instance_id=None, activity_state=None, 
                 activity_name="", comments="", value_add_type=None):
        self.TimeStamp = time_stamp or datetime.now()
        self.ActivityInstanceId = activity_instance_id or uuid.uuid4()
        self.ActivityState = activity_state or ActivityState.Completed
        self.ActivityName = activity_name
        self.Comments = comments
        self.ValueAddType = value_add_type