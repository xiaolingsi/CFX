"""
A specialized type of Activity that occurs within a Selective Soldering System.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from ..Activity import Activity
from ..ValueAddType import ValueAddType


@dataclass_json
@dataclass
class SelectiveActivity(Activity):
    """
    A specialized type of Activity that occurs within a Selective Soldering System.
    """
    
    # The action that occured,
    # examples: Solder Pump, Fluxer, Preheater
    Action: Optional[str] = None

    def __post_init__(self):
        """Set default values after initialization"""
        self.ActivityName = "SELECTIVE ACTION"
        self.ValueAddType = ValueAddType.NonValueAdd