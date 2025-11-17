"""
CFX Production ReworkAndRepair Messages Package

This package contains all rework and repair related message classes.
You can import all rework and repair messages at once using:
    from CFX.Messages.Production.ReworkAndRepair import *
"""

# Import all rework and repair message classes
from .UnitsRepaired import UnitsRepaired

# Define __all__ for explicit exports
__all__ = [
    'UnitsRepaired'
]