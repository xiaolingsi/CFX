from enum import Enum


class WorkStagePauseReason(Enum):
    """
    Types of WorkStage pause reasons
    """
    
    # The reason of the pause is unknown
    Unknown = "Unknown"
    
    # The stage is stopped because a material is missing (or too low quantity) for production
    MaterialMissing = "MaterialMissing"
    
    # The stage is stopped because a nozzle is missing (or too low quantity) for production
    NozzleMissing = "NozzleMissing"
    
    # The stage is waiting for the previous stage ton convey a board to him
    WaitingForPreviousStageConveying = "WaitingForPreviousStageConveying"
    
    # The stage is waiting for the next stage to be able to receive a board
    WaitingForNextStageConveying = "WaitingForNextStageConveying"
    
    # The stage is waiting for the operator to execute a manual alignment
    ManualAlignmentNeeded = "ManualAlignmentNeeded"
    
    # The stage is waiting for the operator to confirm the installation a material (doubt)
    MaterialInstalledConfirmationNeeded = "MaterialInstalledConfirmationNeeded"
    
    # The stage is waiting for the operator to manually fill a barcode
    ManualBarcodeFillingNeeded = "ManualBarcodeFillingNeeded"
    
    # The stage is waiting for the operator to confirm an information message
    InformationMessageConfirmation = "InformationMessageConfirmation"
    
    # ** NOTE: ADDED in CFX 1.2 **
    # The stage is waiting because it has been stopped by the operator
    ProductionStoppedByOperator = "ProductionStoppedByOperator"