"""
CFX Structures Cleaning Package

This package contains all cleaning related structure classes.
You can import all cleaning structures at once using:
    from CFX.Messages.Structures.Cleaning import *
"""

# Import all cleaning structure classes
from .CleaningManagementData import CleaningManagementData
from .CleaningProcessData import CleaningProcessData
from .CleaningReading import CleaningReading
from .CleaningReadingType import CleaningReadingType
from .CleaningState import CleaningState
from .CleaningStep import CleaningStep
from .CleaningStepType import CleaningStepType

# Define __all__ for explicit exports
__all__ = [
    'CleaningManagementData',
    'CleaningProcessData',
    'CleaningReading',
    'CleaningReadingType',
    'CleaningState',
    'CleaningStep',
    'CleaningStepType'
]