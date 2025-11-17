from enum import Enum

class NonInstalledComponentLocation(Enum):
    """Location of a non installed component"""
    
    # The location is unknown, the component is lost
    Lost = "Lost"
    # The component is back to the material carrier
    MaterialCarrier = "MaterialCarrier"
    # The component has been thrown in the rejection box
    RejectionBox = "RejectionBox"