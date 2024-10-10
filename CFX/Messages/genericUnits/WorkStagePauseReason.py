import enum


class WorkStagePauseReason(enum.Enum):
    Unknown = 0
    MaterialMissing = 1
    NozzleMissing = 2
    WaitingForPreviousStageConveying = 3
    WaitingForNextStageConveying = 4
    ManualAlignmentNeeded = 5
    MaterialInstalledConfirmationNeeded = 6
    ManualBarcodeFillingNeeded = 7
    InformationMessageConfirmation = 8
    ProductionStoppedByOperator = 9
