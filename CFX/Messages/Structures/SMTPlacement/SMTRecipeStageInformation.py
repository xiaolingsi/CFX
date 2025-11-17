"""
** NOTE: ADDED in CFX 1.5 **
Describes some information about a recipe for a specific stage, with more information for an SMT machine
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from ..RecipeStageInformation import RecipeStageInformation
from ..Head import Head


@dataclass_json
@dataclass
class SMTRecipeStageInformation(RecipeStageInformation):
    """
    ** NOTE: ADDED in CFX 1.5 **
    Describes some information about a recipe for a specific stage, with more information for an SMT machine
    """
    
    # List of heads that are associated with this stage for the given recipe, if applicable.
    Heads: List[Head] = field(default_factory=list)