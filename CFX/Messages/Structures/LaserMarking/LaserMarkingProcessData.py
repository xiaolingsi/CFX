from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import timedelta
from ..ProcessData import ProcessData

@dataclass_json
@dataclass
class LaserMarkingProcessData(ProcessData):
    """Provides information about the conditions within a reflow oven at a given point in time."""
    
    # Total amount of time that the laser was used during processing.
    LaserProcessingTime: Optional[timedelta] = None
    
    # The name of the active recipe at the time when the processing occurred.
    RecipeName: Optional[str] = None