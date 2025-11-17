from enum import Enum


class TestMethod(Enum):
    """
    Method of testing
    """
    
    # The test was performed by a human being
    Human = "Human"
    
    # The test was performed by automated equipment / device
    Automated = "Automated"
    
    # The test was performed by an in-circuit test equipment / device
    ICT = "ICT"
    
    # The test was performed by a flying probe test machine / equipment / device
    FPT = "FPT"
    
    # The test was performed by a functional test machine / equipment / device
    FCT = "FCT"
    
    # The test was performed by a boundary scan test machine / equipment / deivce
    BST = "BST"