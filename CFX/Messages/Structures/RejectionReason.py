from enum import Enum

class RejectionReason(Enum):
    """Rejection reason"""
    
    # Rejection reason is unknown 
    Unknown = "Unknown"
    # The component was not placed because of a mechanical error
    MechanicalError = "MechanicalError"
    # The component was not placed because of an electrical error
    ElectricalError = "ElectricalError"
    # The component was not placed because of a software error
    SoftwareError = "SoftwareError"
    # The component was not placed because of an error from an external device
    ExternalDeviceError = "ExternalDeviceError"
    # The component was rejected because of a bad electrical test
    BadElectricalTest = "BadElectricalTest"
    # The component was rejected because of a generic error detected after pickup
    ErrorAfterPickUp = "ErrorAfterPickUp"
    # The component was rejected because of a bad vision test after pickup
    BadVisionTestAfterPickup = "BadVisionTestAfterPickup"
    # The component was rejected because of a bad pressure test after pickup
    BadPressureTestAfterPickup = "BadPressureTestAfterPickup"
    # The component was rejected because of a bad optical test after pickup
    BadOpticalTestAfterPickup = "BadOpticalTestAfterPickup"
    # The component was rejected because of a wrong placement
    ErrorAfterPlacement = "ErrorAfterPlacement"
    # The component was rejected because of a bad vision test after placement
    BadVisionTestAfterPlacement = "BadVisionTestAfterPlacement"
    # The component was rejected because of a bad pressure test after placement
    BadPressureTestAfterPlacement = "BadPressureTestAfterPlacement"
    # The component was rejected because of a bad optical test after placement
    BadOpticalTestAfterPlacement = "BadOpticalTestAfterPlacement"
    # ** NOTE: ADDED in CFX 1.4 **
    # The component was rejected because of a bad vision test before pickup
    BadVisionTestBeforePickup = "BadVisionTestBeforePickup"