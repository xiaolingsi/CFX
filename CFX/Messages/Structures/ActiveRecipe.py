from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.RecipeIdentifier import RecipeIdentifier
from CFX.Messages.Structures.Recipe import Recipe


@dataclass_json
@dataclass
class ActiveRecipe(object):
    """
    Represents a recipe active on a certain lane inside of a machine.
    This is equivalent to the information present in a RecipeActivated message
    but represented as a structure so that it can be included in the Heartbeat
    message.
    """
    
    Lane: Optional[int] = None
    Stage: Optional[Stage] = None
    RecipeIdentifier: Optional[RecipeIdentifier] = None
    Recipe: Optional[Recipe] = None

    def __init__(self, lane=None, stage=None, recipe_identifier=None, recipe=None):
        self.Lane = lane
        self.Stage = stage
        self.RecipeIdentifier = recipe_identifier
        self.Recipe = recipe