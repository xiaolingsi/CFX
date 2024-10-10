import enum


class RecipeModificationReason(enum.Enum):
    Unspecified = 0
    NewRecipe = 1
    NewRevision = 2
    UpdatedGeometry = 3
    UpdatedBOM = 4
    PositionalCorrection = 5
    RotationalCorrection = 6
    VisionSystemCorrection = 7
    RecipeDeleted = 8
