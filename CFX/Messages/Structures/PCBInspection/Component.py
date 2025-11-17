from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from .GeometricObject import GeometricObject
from .Pin import Pin

@dataclass_json
@dataclass
class Component(GeometricObject):
    """A component as a resistor, capacitor, IC, ...
    Typically has (two or more) pins (as its "children")."""
    
    def __post_init__(self):
        if self.Pins is None:
            self.Pins = []
    
    # Component type, e.g. "C1206", "R1206", "TO252AA".
    Type: Optional[str] = None
    
    # Group of component classification like "Capacitor", "Resistor", "DPAK".
    Group: Optional[str] = None
    
    # List of Pins of this component.
    Pins: List[Pin] = field(default_factory=list)
    
    # The internal part number of the designated component.
    PartNumber: Optional[str] = None
    
    @property
    def IsDefect(self) -> bool:
        """Checks if this component (or one of its pins) is defect."""
        if self.IsRepaired:
            return False  # The component as a whole was repaired, so it is not defect anymore.
        
        if super().IsDefect:
            return True  # The inspection object itself is defect.
        
        # Check all children recursively.
        for pin in self.Pins:
            if pin.IsDefect:
                return True  # At least one pin is defect, so this inspection object is considered defect.
        
        return False  # No defect in any of our features or pins.