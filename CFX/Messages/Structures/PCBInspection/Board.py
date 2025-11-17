from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from .GeometricObject import GeometricObject
from .Fiducial import Fiducial
from .Component import Component

@dataclass_json
@dataclass
class Board(GeometricObject):
    """A board typically is part of a (multi-)panel and may contain fiducials, components
    (an even sub-boards).
    It is an inspection object itself, too (with features on its own)."""
    
    def __post_init__(self):
        if self.Fiducials is None:
            self.Fiducials = []
        if self.Components is None:
            self.Components = []
        if self.Boards is None:
            self.Boards = []
    
    # This is a list of fiducials.
    Fiducials: List[Fiducial] = field(default_factory=list)
    
    # This is the list of components in the board definition.
    Components: List[Component] = field(default_factory=list)
    
    # List of "sub-boards" of this board.
    # Usually empty, but it allows to have panels with several boards, where each board may have some "sub-boards", even recursivly. 
    Boards: List['Board'] = field(default_factory=list)
    
    # Logical reference of production unit as defined by CFX position rule (see CFX standard)
    UnitPositionNumber: Optional[int] = None
    
    @property
    def IsDefect(self) -> bool:
        """A board is considered defect if there is a defect in (the features / checks of) the board itself
        or in one of its components, fiducials, or sub-boards.
        """
        if self.IsRepaired:
            return False  # The board as a whole was repaired, so it is not defective anymore.
        
        if super().IsDefect:
            return True  # The board itself is defective.
        
        # Check all children recursively.
        for fiducial in self.Fiducials:
            if fiducial.IsDefect:
                return True  # At least one fiducial is defective, so this board is considered defective.
        
        for component in self.Components:
            if component.IsDefect:
                return True  # At least one component is defective, so this board is considered defective.
        
        for board in self.Boards:
            if board.IsDefect:
                return True  # At least one board is defective, so this board is considered defective.
        
        return False  # No defect in any of our features or children.