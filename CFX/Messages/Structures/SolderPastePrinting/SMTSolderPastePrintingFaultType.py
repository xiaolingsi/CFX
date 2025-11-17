"""
Types of SMT printing faults
"""

from enum import Enum
from dataclasses_json import dataclass_json


class SMTSolderPastePrintingFaultType(Enum):
    """
    Types of SMT printing faults
    """
    
    # A squeegee related error
    SqueegeeError = 0
    
    # A paste related error
    PasteError = 1