from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .ProcessingResult import ProcessingResult
from .ProcessData import ProcessData

@dataclass_json
@dataclass
class ProcessedUnit:
    """Structure representing a production units that has been processed at
    an endpoint involved in the processing of production units."""
    
    def __init__(self):
        self.UnitResult = ProcessingResult.Succeeded
    
    # Unique ID of Production Unit, Panel, or Carrier
    UnitIdentifier: Optional[str] = None
    
    # Logical reference of production unit as defined by CFX position rule (see CFX standard)
    UnitPositionNumber: Optional[int] = None
    
    # Indicates the overall result of the processing that was performed on the unit.
    UnitResult: ProcessingResult = ProcessingResult.Succeeded
    
    # Process data specific to this particular production unit.  This may be null if there is 
    # no process data specfific to this individual unit.  For example, if all units processed
    # during the transaction experienced the same conditions, the UnitsProcessed message will
    # contain this information, and the UnitProcessData property will be null.
    UnitProcessData: Optional[ProcessData] = None