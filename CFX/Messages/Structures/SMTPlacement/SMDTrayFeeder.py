"""
Describes an SMT Tray carrier
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from ..MaterialCarrier import MaterialCarrier


@dataclass_json
@dataclass
class SMDTrayFeeder(MaterialCarrier):
    """
    Describes an SMT Tray carrier
    """
    
    # The x dimension of each cell in tray carrier
    CellDimensionX: float = 0.0
    
    # The y dimension of each cell in tray carrier
    CellDimensionY: float = 0.0
    
    # The number of cells in x axis in this tray carrier
    CellCountX: int = 0
    
    # The number of cells in y axis in this tray carrier
    CellCountY: int = 0
    
    # The x offset between adjacent cells in tray carrier
    CellPitchX: float = 0.0
    
    # The y offset between adjacent cells in tray carrier
    CellPitchY: float = 0.0