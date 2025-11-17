"""
** NOTE: ADDED in CFX 1.2 **
Describes the separation structure as modelled in the SolderPastePrintingRecipe
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class Separation:
    """
    ** NOTE: ADDED in CFX 1.2 **
    Describes the separation structure as modelled in the SolderPastePrintingRecipe
    """
    
    # Separation object name for Solder Paste Printing. For future use.
    Name: Optional[str] = None
    
    # Separation speed value for Solder Paste Printing - UpdateRecipeRequest
    SeparationSpeed: Optional[float] = None
    
    # Separation distance for Solder Paste Printing - UpdateRecipeRequest
    SeparationDistance: Optional[float] = None
    
    # Separation delay for Solder Paste Printing. For future use.
    SeparationDelay: Optional[float] = None