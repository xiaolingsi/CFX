import enum


class StatusResult(enum.Enum):
    Success = 0
    PartialSuccess = 1
    Failed = 2
    Warning = 3
