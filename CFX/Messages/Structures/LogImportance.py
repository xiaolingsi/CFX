import enum


class LogImportance(enum.Enum):
    Debug = 0
    Information = 1
    Warning = 2
    Error = 3
    Fatal = 4