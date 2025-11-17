from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, List
import uuid
from CFX.Messages.Structures.ComponentDesignator import ComponentDesignator
from CFX.Messages.Structures.Region import Region
from CFX.Messages.Structures.Image import Image
from CFX.Messages.Structures.Measurement import Measurement
from CFX.Messages.Structures.Symptom import Symptom
from CFX.Messages.Structures.VerificationResult import VerificationResult


@dataclass_json
@dataclass
class Defect(object):
    """
    Describes a defect that was discovered on a production unit
    """
    
    UniqueIdentifier: str
    DefectCode: Optional[str] = None
    DefectCategory: Optional[str] = None
    Description: Optional[str] = None
    Comments: Optional[str] = None
    ComponentOfInterest: Optional[ComponentDesignator] = None
    RegionOfInterest: Optional[Region] = None
    DefectImages: Optional[List[Image]] = None
    Priority: Optional[int] = 0
    ConfidenceLevel: Optional[float] = 0.0
    RelatedMeasurements: Optional[List[Measurement]] = None
    RelatedSymptoms: Optional[List[Symptom]] = None
    Verification: Optional[VerificationResult] = VerificationResult.DefectClosed
    VerificationDetail: Optional[str] = None

    def __init__(self):
        self.UniqueIdentifier = str(uuid.uuid4())