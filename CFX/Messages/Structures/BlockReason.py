from enum import Enum


class BlockReason(Enum):
    """
    Reasons why a unit is blocked
    """
    
    # No reason specified
    Unspecified = "Unspecified"
    
    # There exists suspicion that the material or unit may be defective or otherwise problematic
    SuspectedProblem = "SuspectedProblem"
    
    # The material or unit is known to be defective.
    Defective = "Defective"
    
    # A material has expired, and can no longer be utilized.
    ExpiredMaterial = "ExpiredMaterial"
    
    # A tool has expired, and can no longer be utilized.
    ExpiredTool = "ExpiredTool"