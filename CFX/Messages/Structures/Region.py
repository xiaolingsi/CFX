from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from .Segment import Segment

@dataclass_json
@dataclass
class Region:
    """Describes a planar, 2 dimensional region as defined by a series of X, Y coordinates
    that when plotted, form the region."""
    
    def __post_init__(self):
        if self.RegionSegments is None:
            self.RegionSegments = []
    
    # X coordinate of first point in region outline
    StartPointX: float = 0.0
    
    # Y coordinate of first point in region outline
    StartPointY: float = 0.0
    
    # Collection of (X, Y) coordinates that when plotted form a planar region.
    RegionSegments: List[Segment] = field(default_factory=list)