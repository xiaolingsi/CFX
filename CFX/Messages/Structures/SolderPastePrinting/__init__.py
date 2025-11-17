"""
CFX Structures SolderPastePrinting Package

This package contains all solder paste printing related structure classes.
You can import all solder paste printing structures at once using:
    from CFX.Messages.Structures.SolderPastePrinting import *
"""

# Import all solder paste printing structure classes
from .PeriodicCleaning import PeriodicCleaning
from .Separation import Separation
from .SMTSolderPastePrintingFault import SMTSolderPastePrintingFault
from .SMTSolderPastePrintingFaultType import SMTSolderPastePrintingFaultType
from .SMTSqueegee import SMTSqueegee
from .SMTSqueegeeCleanType import SMTSqueegeeCleanType
from .SMTStencil import SMTStencil
from .SMTStencilCleanMode import SMTStencilCleanMode
from .SolderPastePrintingPCBProcessData import SolderPastePrintingPCBProcessData

# Define __all__ for explicit exports
__all__ = [
    'PeriodicCleaning',
    'Separation',
    'SMTSolderPastePrintingFault',
    'SMTSolderPastePrintingFaultType',
    'SMTSqueegee',
    'SMTSqueegeeCleanType',
    'SMTStencil',
    'SMTStencilCleanMode',
    'SolderPastePrintingPCBProcessData'
]