from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from datetime import datetime

from CFX.CFXUtils import CFXUtils


@dataclass_json
@dataclass
class EnvironmentalCondition(object):
    """
    Describes an environmental condition that was in place when an action was performed.
    """
    
    StartTime: Optional[datetime] = CFXUtils.get_iso8601_time()
    EndTime: Optional[datetime] = CFXUtils.get_iso8601_time()
    MeanValue: float = 0.0
    MedianValue: float = 0.0
    MaxValue: float = 0.0
    MinValue: float = 0.0