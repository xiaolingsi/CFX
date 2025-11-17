"""
CFX Production Assembly PressInsertion Messages Package

This package contains all press insertion related message classes.
You can import all press insertion messages at once using:
    from CFX.Messages.Production.Assembly.PressInsertion import *
"""

# Import all press insertion message classes
from .ConditionCompleted import ConditionCompleted
from .GetConditionPermissionRequest import GetConditionPermissionRequest
from .GetConditionPermissionResponse import GetConditionPermissionResponse

# Define __all__ for explicit exports
__all__ = [
    'ConditionCompleted',
    'GetConditionPermissionRequest',
    'GetConditionPermissionResponse'
]