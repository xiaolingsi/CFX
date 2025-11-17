"""
** NOTE: ADDED in CFX 1.2 **
Describes the stroke structure as modelled in the SolderPastePrintingRecipe
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from enum import Enum


@dataclass_json
@dataclass
class Stroke:
    """
    ** NOTE: ADDED in CFX 1.2 **
    Describes the stroke structure as modelled in the SolderPastePrintingRecipe
    """
    
    # Stroke property Print pressure
    PrintPressure: Optional[float] = None
    
    # Stroke property Print speed
    PrintSpeed: Optional[float] = None


class SolderPasteSqueegeeDirection(Enum):
    """
    Squeegee direction enumeration
    """
    
    # Forward
    forward = 0
    
    # Backward
    backward = 1