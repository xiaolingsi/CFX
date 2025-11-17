from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class SleepState:
    """
    ** NOTE: ADDED in CFX 1.3 **
    Definition of Sleep State
    """
    
    # A descriptive name for this sleep state
    SleepName: str = "Awake"
    
    # Power consumption saving achieved through this sleep state.
    # PowerSaving units are percentages
    PowerSaving: float = 0.0
    
    # Time interval required to go from the current sleep state to the "Awake" state.
    # WakeupTime units are seconds
    WakeupTime: float = 0.0