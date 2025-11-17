from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ComponentDesignator import ComponentDesignator
from CFX.Messages.Structures.Region import Region
from CFX.Messages.Structures.Measurement import Measurement
from CFX.Messages.Structures.IssueStatus import IssueStatus


@dataclass_json
@dataclass
class Symptom(object):
    """
    Describes a situation where a problem is identified via one or more failed tests.
    A symptom does not identify the actual cause of the failure(s), only that 
    there is a problem that needs to be investigated. 
    """
    
    # A unique identifier for this particular symptom instance
    # (new and unique each time a new symptom is discovered).
    UniqueIdentifier: str = ""
    
    # A code identifying the type of symptom
    SymptomCode: str = ""
    
    # An optional symptom category for this particular type of symptom
    SymptomCategory: str = ""
    
    # A human friendly description of the symptom
    Description: str = ""
    
    # Optional comments from the tester who discovered this symptom
    Comments: str = ""
    
    # An enumeration describing the current status of the symptom as it progresses through it's lifecycle.
    # NOTE: ADDED in CFX 1.4
    Status: IssueStatus = IssueStatus.ISFalse
    
    # A list of the components or specific component pins related to this symptom (if known)
    ComponentsOfInterest: List[ComponentDesignator] = field(default_factory=list)
    
    # An optional location or area on the production unit where the symptom is located 
    # (for cases where there is no specific components that can be definitively related).
    RegionOfInterest: Optional[Region] = None
    
    # The priority of this symptom as compared to other symptom discovered for this unit.
    # A priority of 1 indicates the highest priority.
    Priority: int = 1
    
    # A list of measurements that were taken which caused this symptom to be created
    RelatedMeasurements: List[Measurement] = field(default_factory=list)
    
    def __init__(self, uniqueIdentifier="", symptomCode="", symptomCategory="", description="", 
                 comments="", status=IssueStatus.ISFalse, componentsOfInterest=None,
                 regionOfInterest=None, priority=1, relatedMeasurements=None):
        self.UniqueIdentifier = uniqueIdentifier
        self.SymptomCode = symptomCode
        self.SymptomCategory = symptomCategory
        self.Description = description
        self.Comments = comments
        self.Status = status
        self.ComponentsOfInterest = componentsOfInterest if componentsOfInterest is not None else []
        self.RegionOfInterest = regionOfInterest
        self.Priority = priority
        self.RelatedMeasurements = relatedMeasurements if relatedMeasurements is not None else []