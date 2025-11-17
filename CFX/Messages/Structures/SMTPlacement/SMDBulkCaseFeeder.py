"""
** NOTE: ADDED in CFX 1.5 **
Describes an Bulk Case feeder.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from ..MaterialCarrier import MaterialCarrier


@dataclass_json
@dataclass
class SMDBulkCaseFeeder(MaterialCarrier):
    """
    ** NOTE: ADDED in CFX 1.5 **
    Describes an Bulk Case feeder.
    """
    
    # The x dimension of each cell in this Bulk Case feeder
    CellDimensionX: float = 0.0
    
    # The y dimension of each cell in this Bulk Case feeder
    CellDimensionY: float = 0.0
    
    # The number of cells in x axis in this Bulk Case feeder
    CellCountX: int = 0
    
    # The number of cells in y axis in this Bulk Case feeder
    CellCountY: int = 0
    
    # The x offset between adjacent cells in this Bulk Case feeder
    CellPitchX: float = 0.0
    
    # The y offset between adjacent cells in this Bulk Case feeder
    CellPitchY: float = 0.0