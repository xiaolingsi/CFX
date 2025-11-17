from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Recipe:
    """Represents a collection of instructions used by a piece of automated equipment to perform
    a function (typically upon a production unit) during production."""
    
    # The name of the recipe (may include full path, if applicable)
    Name: Optional[str] = None
    
    # An optional version number, e.g. "2.0"
    Revision: Optional[str] = None
    
    # The total amount of time that is expected to process one unit or group of units (as in the case of a carrier or panelized PCB), 
    # assuming no blocked or starved conditions at the station.  This includes both productive and non-productive time, such as transfer, 
    # positioning, etc.
    ExpectedCycleTime: float = 0.0
    
    # ** NOTE: ADDED in CFX 1.6 **
    # The total amount of productive time (in ms) that is expected to process one unit or group of units (as in the case of a carrier or panelized PCB),
    # assuming no blocked or starved conditions at the station. This does not include any non-productive time, such as transfer, positioning, etc.
    ExpectedWorkTime: Optional[float] = 0.0
    
    # The number of units that are to be processed simulataneously by this recipe.  For example, in the case of a 2 x 2 panelized PCB, this
    # property would be 4 because 4 units (PCB's) are procesed at one time per work transaction.  In the case that a station processes a
    # variable number of units per transaction, this should represent the average number of units expected to be processed per transaction.
    ExpectedUnitsPerWorkTransaction: float = 0.0
    
    # ** NOTE: ADDED in CFX 1.2 **
    # Length (X-Axis) of the Units processed within this Recipe, in centimeters.  Parallel to direction of production flow.
    UnitLength: Optional[float] = None
    
    # ** NOTE: ADDED in CFX 1.2 **
    # Width (Y-Axis) of the Units processed within this Recipe, in centimeters.  Perpendicular to direction of production flow when viewed from above.
    UnitWidth: Optional[float] = None
    
    # ** NOTE: ADDED in CFX 1.2 **
    # Heigth (Z-Axis) of the Units processed within this Recipe, in centimeters.  Perpendicular to direction of production flow when viewed from the side.
    UnitHeight: Optional[float] = None
    
    # The MIME type of the binary data contained by the RecipeData property.
    MimeType: Optional[str] = None
    
    # A binary representation of the recipe data.
    RecipeData: Optional[bytes] = None