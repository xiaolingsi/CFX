from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, List
from datetime import datetime
from CFX.Messages.Structures.Defect import Defect
from CFX.Messages.Structures.Measurement import Measurement
from CFX.Messages.Structures.Symptom import Symptom
from CFX.Messages.Structures.TestResult import TestResult
from CFX.Messages.Structures.VerificationResult import VerificationResult


@dataclass_json
@dataclass
class Inspection(object):
    """
    Describes a single step in a series of steps that an inspector makes (both human or automation)
    in the course of inspecting a production unit.
    """
    
    UniqueIdentifier: Optional[str] = None
    InspectionName: Optional[str] = None
    InspectionStartTime: Optional[datetime] = None
    InspectionEndTime: Optional[datetime] = None
    TestProcedure: Optional[str] = None
    Comments: Optional[str] = None
    Result: Optional[TestResult] = None
    Verification: Optional[VerificationResult] = None
    VerificationDetail: Optional[str] = None
    Error: Optional[str] = None
    DefectsFound: Optional[List[Defect]] = None
    Symptoms: Optional[List[Symptom]] = None
    Measurements: Optional[List[Measurement]] = None
    RefNo: Optional[int] = None

    def __init__(self):
        self.DefectsFound = []
        self.Measurements = []
        self.Symptoms = []