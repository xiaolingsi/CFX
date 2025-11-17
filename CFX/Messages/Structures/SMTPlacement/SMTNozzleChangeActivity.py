"""
A specialized type of Activity that occurs when a unit is loaded into an endpoint.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
import uuid
from datetime import datetime
from ..Activity import Activity
from ..ValueAddType import ValueAddType
from ..ActivityState import ActivityState
from .SMTHeadAndNozzle import SMTHeadAndNozzle


@dataclass_json
@dataclass
class SMTNozzleChangeActivity(Activity):
    """
    A specialized type of Activity that occurs when a unit is loaded into an endpoint.
    """
    
    # The nozzles that were removed (if known)
    OldNozzles: List[SMTHeadAndNozzle] = field(default_factory=list)
    
    # The new nozzles that were loaded (mandatory)
    NewNozzles: List[SMTHeadAndNozzle] = field(default_factory=list)

    def __init__(self, time_stamp=None, activity_instance_id=None, activity_state=None, 
                 activity_name="NOZZLE CHANGE", comments="", value_add_type=None):
        super().__init__(
            time_stamp=time_stamp or datetime.now(),
            activity_instance_id=activity_instance_id or uuid.uuid4(),
            activity_state=activity_state or ActivityState.Completed,
            activity_name=activity_name,
            comments=comments,
            value_add_type=value_add_type or ValueAddType.NonValueAdd
        )