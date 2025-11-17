from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RecipeIdentifier:
    """** NOTE: ADDED in CFX 1.4 **
    Represents a collection of instructions used by a piece of automated equipment to perform
    a function (typically upon a production unit) during production. The RecipeLean does not deliver the Recipe data
    but RecipeName and Revision only. For the full Recipe data, please see Recipe."""
    
    # The name of the recipe (may include full path, if applicable)
    RecipeName: Optional[str] = None
    
    # An optional version number, e.g. "2.0"
    Revision: Optional[str] = None