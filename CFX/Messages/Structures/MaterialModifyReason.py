from enum import Enum

class MaterialModifyReason(Enum):
    """Reason why the attributes of a material package were modified"""
    
    # No reason specified
    Unspecified = "Unspecified"
    # Correction of incorrect information
    InformationWasIncorrect = "InformationWasIncorrect"
    # Quantity updated after manual count / measurement
    ManualCountAndQuantityUpdate = "ManualCountAndQuantityUpdate"
    # The sensor triggered correction, which is typically the quantity correction when a splice is been detected.
    SensorTriggeredCorrection = "SensorTriggeredCorrection"