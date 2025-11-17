from enum import Enum

class UVCuringLampState(Enum):
    """
    An enumeration indicating the state of lamp.
    ** NOTE: ADDED in CFX 1.6 **
    """
    On = "On"
    Off = "Off"
    Error = "Error"