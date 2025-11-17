"""
Modes of stencil cleaning
"""

from enum import Enum
from dataclasses_json import dataclass_json


class SMTStencilCleanMode(Enum):
    """
    Modes of stencil cleaning
    """
    
    # Clean mode W - wet clean: printer uses a cleaning liquid to wipe the stencil
    W = "W"
    
    # Clean mode V - vacuum clean: printer is using vacuum cleaner to dry up cleaning liquid or to
    # support cleaning strokes
    V = "V"
    
    # Clean mode D - dry clean: printer wipes the stencil with a dry fabric
    D = "D"