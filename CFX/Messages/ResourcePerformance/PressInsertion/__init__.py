"""
CFX ResourcePerformance PressInsertion Messages Package

This package contains all press insertion related message classes.
You can import all press insertion messages at once using:
    from CFX.Messages.ResourcePerformance.PressInsertion import *
"""

# Import all press insertion message classes
from .ComponentsPressed import ComponentsPressed

# Define __all__ for explicit exports
__all__ = [
    'ComponentsPressed'
]