from enum import Enum


class IssueStatus(Enum):
    """
    An enumeration which describes the lifecycle of an issue, such as a Defect or Symptom
    """
    
    NewlyDiscovered = "NewlyDiscovered"
    Confirmed = "Confirmed"
    ISFalse = "False"
    Repaired = "Repaired"
    Closed = "Closed"