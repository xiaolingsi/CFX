from enum import Enum


class TestResult(Enum):
    """
    Result of a test or inspection
    """
    
    Passed = "Passed"
    Failed = "Failed"
    Skipped = "Skipped"