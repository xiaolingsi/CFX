import enum


class WorkResult(enum.Enum):
    Completed = 0
    Failed = 1
    Aborted = 2
    Skipped = 3
