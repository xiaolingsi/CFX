"""
CFX Structures SolderReflow Package

This package contains all solder reflow related structure classes.
You can import all solder reflow structures at once using:
    from CFX.Messages.Structures.SolderReflow import *
"""

# Import all solder reflow structure classes
from .ReflowOvenFault import ReflowOvenFault
from .ReflowOvenFaultType import ReflowOvenFaultType
from .ReflowOvenParameter import ReflowOvenParameter
from .ReflowProcessData import ReflowProcessData
from .ReflowReading import ReflowReading
from .ReflowReadingType import ReflowReadingType
from .ReflowSetPoint import ReflowSetPoint
from .ReflowSetpointType import ReflowSetpointType
from .ReflowSubZoneType import ReflowSubZoneType
from .ReflowZone import ReflowZone
from .ReflowZoneData import ReflowZoneData

# Define __all__ for explicit exports
__all__ = [
    'ReflowOvenFault',
    'ReflowOvenFaultType',
    'ReflowOvenParameter',
    'ReflowProcessData',
    'ReflowReading',
    'ReflowReadingType',
    'ReflowSetPoint',
    'ReflowSetpointType',
    'ReflowSubZoneType',
    'ReflowZone',
    'ReflowZoneData'
]