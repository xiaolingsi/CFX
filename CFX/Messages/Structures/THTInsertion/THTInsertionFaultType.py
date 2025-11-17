from enum import Enum

class THTInsertionFaultType(Enum):
    """
    Types of Through Hole Device Insertion Faults
    """
    XAxisError = "XAxisError"
    YAxisError = "YAxisError"
    ZAxisError = "ZAxisError"
    InsertionError = "InsertionError"
    AlignmentError = "AlignmentError"
    PickupError = "PickupError"
    PartsExhaustedError = "PartsExhaustedError"
    AnvilError = "AnvilError"
    ClinchError = "ClinchError"
    PanelLocationError = "PanelLocationError"
    AirSupplyDown = "AirSupplyDown"