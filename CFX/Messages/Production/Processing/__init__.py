"""
CFX Production Processing Messages Package

This package contains all processing related message classes.
You can import all processing messages at once using:
    from CFX.Messages.Production.Processing import *
"""

# Import all processing message classes
from .UnitsProcessed import UnitsProcessed

# Define __all__ for explicit exports
__all__ = [
    'UnitsProcessed'
]