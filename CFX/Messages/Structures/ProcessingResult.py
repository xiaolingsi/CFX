import enum


class ProcessingResult(enum.Enum):
    Succeeded = 0
    Failed = 1
    Error = 2
    Aborted = 3
    Skipped = 4