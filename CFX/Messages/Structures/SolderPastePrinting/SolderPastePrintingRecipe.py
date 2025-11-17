"""
** NOTE: ADDED in CFX 1.2 **
Describes the Solder paste printing structure 
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from ..Recipe import Recipe
from .Stroke import Stroke
from .Separation import Separation
from .PeriodicCleaning import PeriodicCleaning


@dataclass_json
@dataclass
class SolderPastePrintingRecipe(Recipe):
    """
    ** NOTE: ADDED in CFX 1.2 **
    Describes the Solder paste printing structure 
    """
    
    # List of Stroke objects for Solder Paste Printing
    Strokes: List[Stroke] = field(default_factory=list)
    
    # Print gap value 
    PrintGap: Optional[float] = None
    
    # Separation object 
    Separation: Optional[Separation] = None
    
    # Periodic cleaning object List. Normally it shall be one, but in this way it may be extended more easily 
    PeriodicCleanings: List[PeriodicCleaning] = field(default_factory=list)