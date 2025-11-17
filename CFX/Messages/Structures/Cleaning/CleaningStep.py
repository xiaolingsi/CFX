from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Cleaning.CleaningStepType import CleaningStepType
from CFX.Messages.Structures.Cleaning.CleaningReading import CleaningReading


@dataclass_json
@dataclass
class CleaningStep(object):
    """
    Cleaning step of the cleaning process
    NOTE: ADDED in CFX 1.5
    """
    
    # Cleaning step type
    CleaningStepType: CleaningStepType = CleaningStepType.PreWash
    
    # Elapsed time for cleaning step expressed in seconds (s)
    CleaningStepTime: float = 0.0
    
    # A list of readings / measurements that have been taken for this cleaning step
    Readings: List[CleaningReading] = field(default_factory=list)
    
    def __init__(self, cleaningStepType=CleaningStepType.PreWash, cleaningStepTime=0.0, readings=None):
        self.CleaningStepType = cleaningStepType
        self.CleaningStepTime = cleaningStepTime
        self.Readings = readings if readings is not None else []