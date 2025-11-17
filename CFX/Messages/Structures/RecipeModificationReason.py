from enum import Enum

class RecipeModificationReason(Enum):
    """Reasons why a recipe was modified at an endpoint"""
    
    # Unspecified reason
    Unspecified = "Unspecified"
    # Newly created recipe
    NewRecipe = "NewRecipe"
    # New revision of an existing recipe
    NewRevision = "NewRevision"
    # Geometric information was updated
    UpdatedGeometry = "UpdatedGeometry"
    # Bill of Materials information was updated
    UpdatedBOM = "UpdatedBOM"
    # Correction to positional information
    PositionalCorrection = "PositionalCorrection"
    # Correction to rotational information
    RotationalCorrection = "RotationalCorrection"
    # Correction to information needed by vision system.
    VisionSystemCorrection = "VisionSystemCorrection"
    # ** NOTE: ADDED in CFX 1.2 **
    # The recipe has been deleted
    RecipeDeleted = "RecipeDeleted"