import enum


class FaultSeverity(enum.Enum):
    Information = 0
    Warning = 1
    Error = 2
    Alarm = 3