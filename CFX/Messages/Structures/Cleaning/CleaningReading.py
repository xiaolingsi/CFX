from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Cleaning.CleaningReadingType import CleaningReadingType


@dataclass_json
@dataclass
class CleaningReading(object):
    """
    Cleaning readings / measurements that have been taken during the cleaning process
    NOTE: ADDED in CFX 1.5
    """
    
    # The type of reading 
    ReadingType: CleaningReadingType = CleaningReadingType.BottomSprayBarsPressure
    
    # The value of the reading (expressed in the appropriate units for the ReadingType)
    ReadingValue: Optional[float] = 0.0
    
    def __init__(self, readingType=CleaningReadingType.BottomSprayBarsPressure, readingValue=None):
        self.ReadingType = readingType
        self.ReadingValue = readingValue