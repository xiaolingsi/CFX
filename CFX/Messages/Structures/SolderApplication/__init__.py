"""
CFX Structures SolderApplication Package

This package contains all solder application related structure classes.
You can import all solder application structures at once using:
    from CFX.Messages.Structures.SolderApplication import *
"""

# Import all solder application structure classes
from .SelectiveActivity import SelectiveActivity
from .SelectiveSolderData import SelectiveSolderData
from .SelectiveSolderedPCB import SelectiveSolderedPCB
from .SelectiveSolderPCBProcessData import SelectiveSolderPCBProcessData
from .SelectiveSolderProcessData import SelectiveSolderProcessData
from .ZoneData import ZoneData

# Define __all__ for explicit exports
__all__ = [
    'SelectiveActivity',
    'SelectiveSolderData',
    'SelectiveSolderedPCB',
    'SelectiveSolderPCBProcessData',
    'SelectiveSolderProcessData',
    'ZoneData'
]