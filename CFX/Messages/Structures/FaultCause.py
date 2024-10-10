import enum


class FaultCause(enum.Enum):
    LoadError = 0
    UnloadError = 1
    AutoSafetyStop = 2
    SafetyStop = 3
    QualityCheck = 4
    RemoteStop = 5
    MechanicalFailure = 6
    SoftwareFailure = 7
    PowerFailure = 8
    MissingDocumentation = 9
    Refill = 10
    MsdExpired = 11
    MaterialExpired = 12
    MissingComponent = 13
    ElectricalFailure = 14
    ServicesFailure = 15
    ProcessError = 16
    RejectedComponent = 17
