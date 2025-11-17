"""
Types of SMT stencil cleans
"""

from enum import Enum
from dataclasses_json import dataclass_json


class SMTSqueegeeCleanType(Enum):
    """
    Types of SMT stencil cleans
    """
    
    # A typical clean
    Normal = 0
    
    # A more involved, deeper clean
    Deep = 1
    
    # A fast, light clean
    Quick = 2