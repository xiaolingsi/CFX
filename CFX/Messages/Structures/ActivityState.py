from enum import Enum


class ActivityState(Enum):
    """
    Describes the state of an activity.
    """
    
    Started = "Started"
    Aborted = "Aborted"
    Completed = "Completed"
    On = "On"
    Off = "Off"