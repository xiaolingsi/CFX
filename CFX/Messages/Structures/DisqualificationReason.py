from enum import Enum


class DisqualificationReason(Enum):
    """
    Describes the reason why a production units was disqualified (scrapped)
    """
    
    DefectiveRepairNotPossible = "DefectiveRepairNotPossible"
    DefectiveRepairNotFeasible = "DefectiveRepairNotFeasible"
    DefectiveMaterials = "DefectiveMaterials"