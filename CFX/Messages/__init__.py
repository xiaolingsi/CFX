"""
CFX Messages Package

This package provides all CFX message classes for communication between endpoints.
You can import all messages at once using:
    from CFX.Messages import *

Or import specific message categories:
    from CFX.Messages.ResourcePerformance import *
    from CFX.Messages.Production import *
    from CFX.Messages.Materials import *
    etc.
"""

# Import all message categories
from . import CoreCommunication
from . import genericUnits
from . import InformationSystem
from . import Maintenance
from . import Materials
from . import Production
from . import ResourcePerformance
from . import Structures

# Define __all__ for explicit exports
__all__ = [
    'CoreCommunication',
    'genericUnits', 
    'InformationSystem',
    'Maintenance',
    'Materials',
    'Production',
    'ResourcePerformance',
    'Structures'
]