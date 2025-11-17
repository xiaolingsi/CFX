"""
CFX Production Application Solder Messages Package

This package contains all solder related message classes.
You can import all solder messages at once using:
    from CFX.Messages.Production.Application.Solder import *
"""

# Import all solder message classes
from .PCBSelectiveSoldered import PCBSelectiveSoldered

# Define __all__ for explicit exports
__all__ = [
    'PCBSelectiveSoldered'
]