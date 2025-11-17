"""
** NOTE: ADDED in CFX 1.3 **
Provides recipe information for Solder Paste Inspection devices. It was designed to provide context information for the
existing UnitsInspected message
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from datetime import datetime
from ..Recipe import Recipe
from ..InspectionMethod import InspectionMethod
from ..FiducialInfo import FiducialInfo
from .UnitToInspect import UnitToInspect


@dataclass_json
@dataclass
class SolderPasteInspectionRecipe(Recipe):
    """
    ** NOTE: ADDED in CFX 1.3 **
    Provides recipe information for Solder Paste Inspection devices. It was designed to provide context information for the
    existing UnitsInspected message
    """
    
    # Provides the static recipe information for each Unit that is to be inspected
    UnitsToInspect: List[UnitToInspect] = field(default_factory=list)
    
    # Generation data of the recipe
    RecipeGenerationDate: Optional[datetime] = None
    
    # Describes how the inspections were performed
    InspectionMethod: Optional[InspectionMethod] = None
    
    # ** NOTE: ADDED in CFX 1.6 **
    # This structure represents a Fiducial element. It is used to enrich the panel
    Fiducials: List[FiducialInfo] = field(default_factory=list)