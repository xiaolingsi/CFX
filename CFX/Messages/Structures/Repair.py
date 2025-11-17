from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from datetime import datetime
import uuid
from .ComponentDesignator import ComponentDesignator
from .Region import Region
from .Defect import Defect
from .Symptom import Symptom
from .RepairResult import RepairResult

@dataclass_json
@dataclass
class Repair:
    """** NOTE: ADDED in CFX 1.4 **
    Describes a single repair that was performed on a production unit in the course of rework and/or repair."""
    
    def __post_init__(self):
        if self.RelatedDefectIdentifiers is None:
            self.RelatedDefectIdentifiers = []
        if self.ReclassifiedDefects is None:
            self.ReclassifiedDefects = []
        if self.RelatedSymptomIdentifiers is None:
            self.RelatedSymptomIdentifiers = []
        if self.ReclassifiedSymptoms is None:
            self.ReclassifiedSymptoms = []
    
    # A unique indentifier describing a particular repair.
    # Each new occurrence or recurrence of this same repair a new unique identifier.
    UniqueIdentifier: Optional[str] = None
    
    # Identifies the nature of the repair performed.
    RepairName: Optional[str] = None
    
    # Indicates the time when this particular repair began (if known)
    RepairStartTime: Optional[datetime] = None
    
    # Indicates the time when this particular repair ended (if known)
    RepairEndTime: Optional[datetime] = None
    
    # Optional comments from the person who performed this repair
    Comments: Optional[str] = None
    
    # An optional component or specific component pins related to this repair.
    ComponentOfInterest: Optional[ComponentDesignator] = None
    
    # An optional location or area on the production unit where the repair is located 
    # (for cases where there is no specific component related, such as a scratch or 
    # cosmetic defect).
    RegionOfInterest: Optional[Region] = None
    
    # A list of the unique identifiers of the previously reported defects to which
    # this repair relates.  It is assumed that if the repair is successful, these defects
    # may be considered repaired.
    RelatedDefectIdentifiers: List[str] = field(default_factory=list)
    
    # If previously reported defects are re-classified during the repair process, the updated details of those
    # defects may be reported using this property.
    ReclassifiedDefects: List[Defect] = field(default_factory=list)
    
    # A list of the unique identifiers of the previously reported symptoms (faulty test results) to which
    # this repair relates.  It is assumed that if the repair is successful, these symptoms
    # may be considered resolved.
    RelatedSymptomIdentifiers: List[str] = field(default_factory=list)
    
    # If previously reported symptoms (faulty test results) are re-classified during the repair process, the updated details of those
    # symptoms may be reported using this property.
    ReclassifiedSymptoms: List[Symptom] = field(default_factory=list)
    
    # The overall result of the repair
    Result: Optional[RepairResult] = RepairResult.RepairSuccessful
    
    # In the case that the repair cannot be completed, the error that was the cause of this outcome.
    Error: Optional[str] = None