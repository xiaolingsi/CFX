"""
CFX ResourcePerformance THTInsertion Messages Package

This package contains all THT insertion related message classes.
You can import all THT insertion messages at once using:
    from CFX.Messages.ResourcePerformance.THTInsertion import *
"""

# Import all THT insertion message classes
from .ComponentsInserted import ComponentsInserted

# Define __all__ for explicit exports
__all__ = [
    'ComponentsInserted'
]