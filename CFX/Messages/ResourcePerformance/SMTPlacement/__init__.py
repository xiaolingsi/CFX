"""
CFX ResourcePerformance SMTPlacement Messages Package

This package contains all SMT placement related message classes.
You can import all SMT placement messages at once using:
    from CFX.Messages.ResourcePerformance.SMTPlacement import *
"""

# Import all SMT placement message classes
from .ComponentsPlaced import ComponentsPlaced

# Define __all__ for explicit exports
__all__ = [
    'ComponentsPlaced'
]