"""
CFX Production Assembly Messages Package

This package contains all assembly related message classes.
You can import all assembly messages at once using:
    from CFX.Messages.Production.Assembly import *
"""

# Import all assembly message classes
from .MaterialsInstalled import MaterialsInstalled
from .MaterialsUninstalled import MaterialsUninstalled
from .UnitsPersonalized import UnitsPersonalized

# Import subpackages
from . import PressInsertion

# Define __all__ for explicit exports
__all__ = [
    'MaterialsInstalled',
    'MaterialsUninstalled',
    'UnitsPersonalized',
    'PressInsertion'
]