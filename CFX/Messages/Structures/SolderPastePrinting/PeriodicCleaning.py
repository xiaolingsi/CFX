"""
** NOTE: ADDED in CFX 1.2 **
Describes the periodic cleaning structure as modelled in the SolderPastePrintingRecipe
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class PeriodicCleaning:
    """
    ** NOTE: ADDED in CFX 1.2 **
    Describes the periodic cleaning structure as modelled in the SolderPastePrintingRecipe
    """
    
    # After how many Panels the Printer executes the cleaning process - nominal clean rate
    CleanFrequency: Optional[int] = None
    
    # Clean mode - string to enable combination of values
    # In a second stage, an enum could be defined
    CleanMode: Optional[str] = None