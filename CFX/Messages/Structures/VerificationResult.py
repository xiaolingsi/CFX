from enum import Enum


class VerificationResult(Enum):
    """
    There is a certain workflow after detection of a defective board. Usually a defective board has to be classified,
    i.e. an operator or process engineer has to confirm whether inspection result is a real defect or a false fail (false call) error.
    The Verification Result is 
    """
    
    # The defect which was detected is not classified
    NotVerifiedYet = 0
    
    # The defect which was detected is confirmed 
    DefectConfirmed = 1
    
    # The defect which was detected is rejected "FalseFail"
    DefectRejected = 2
    
    # NOTE: ADDED in CFX 1.5
    # The defect which was detected is rejected "FalseFail", but corrective
    # action for SMT process shall be initiated
    DefectAccepted = 3
    
    # NOTE: ADDED in CFX 1.5
    # The defect which was detected is repaired 
    DefectRepaired = 4
    
    # NOTE: ADDED in CFX 1.5
    # The defect which was detected is repaired and successful repair confirmed
    DefectClosed = 5