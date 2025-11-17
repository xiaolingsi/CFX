from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from .InspectionObject import InspectionObject
from .Fiducial import Fiducial
from .Board import Board
from .Component import Component
from ..Geometry.Vector3 import Vector3

@dataclass_json
@dataclass
class Panel(InspectionObject):
    """The root element for the CFX recipe export."""
    
    def __post_init__(self):
        if self.Fiducials is None:
            self.Fiducials = []
        if self.Boards is None:
            self.Boards = []
        if self.Components is None:
            self.Components = []
    
    # Name of the assembly variant. May be empty.
    Variant: Optional[str] = None
    
    # Size of the panel (in µm).
    Size: Optional[Vector3] = None
    
    # The list of fiducials of this panel.
    # (Only the top-level fiducials, not the fiducials of a board.)
    Fiducials: List[Fiducial] = field(default_factory=list)
    
    # The list of boards, that are part of this panel.
    # (Only the top-level boards, not the sub-boards of a top-level board.)
    Boards: List[Board] = field(default_factory=list)
    
    # List of components directly assigned to this panel, not those assigned to one of its boards.
    # Usually empty (as a panel consist of n boards), but allows to omit boards and assign the components directly to the panel.
    Components: List[Component] = field(default_factory=list)
    
    @property
    def IsDefect(self) -> bool:
        """A panel is considered defect if there is a defect in (the features / checks of) the panel itself
        or in one of its fiducials, boards, or components.
        Even if a panel is defective, one of its boards can still be (and typically will be) Ok. 
        """
        if self.IsRepaired:
            return False  # The panel as a whole was repaired, so it is not a defect anymore.
        
        if super().IsDefect:
            return True  # The panel itself is defective.
        
        # Check all children recursively.
        for fiducial in self.Fiducials:
            if fiducial.IsDefect:
                return True  # At least one fiducial is defective, so this panel is considered defective.
        
        for board in self.Boards:
            if board.IsDefect:
                return True  # At least one board is defective, so this panel is considered defective.
        
        for component in self.Components:
            if component.IsDefect:
                return True  # At least one component is defective, so this panel is considered defective.
        
        return False  # No defect in any of our features or children.