from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from ..NamedObject import NamedObject
from .Feature import Feature

@dataclass_json
@dataclass
class InspectionObject(NamedObject):
    """Representing a physical object (panel, board, component, fiducial, pin) with features to check
    during inspection."""
    
    def __post_init__(self):
        if self.Features is None:
            self.Features = []
    
    # Features to check during inspection, like "Presence", "Displacement", "Height".
    Features: List[Feature] = field(default_factory=list)
    
    # The inspection object as a whole was repaired. (E.g. by replacing the whole component.)
    IsRepaired: bool = False
    
    @property
    def IsDefect(self) -> bool:
        """The inspection object is defective, i.e.
        - it was detected as defect,
        - not verified as "false call",  and
        - not repaired.
        """
        if self.IsRepaired:
            return False  # The component as a whole was repaired, so it is not defect anymore.
        
        for feature in self.Features:
            if feature.IsDefect:
                return True  # At least one feature is defective, so this inspection object is defective.
        
        return False  # No defect in any of our features.