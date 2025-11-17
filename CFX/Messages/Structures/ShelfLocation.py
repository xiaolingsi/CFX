from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .LocationDetail import LocationDetail
from .ShelfSideLocation import ShelfSideLocation


@dataclass_json
@dataclass
class ShelfLocation(LocationDetail):
    """
    ** NOTE: ADDED in CFX 1.7 **
    Describes a shelf location
    """
    
    # The shelf side location
    SideLocation: ShelfSideLocation = ShelfSideLocation.Unknown
    
    # The number of rows of the shelf
    RowCount: float = 0.0
    
    # The number of columns of the shelf
    ColumnCount: float = 0.0
    
    # The specific row of the shelf of the location
    Row: float = 0.0
    
    # The specific column of the shelf of the location
    Column: float = 0.0