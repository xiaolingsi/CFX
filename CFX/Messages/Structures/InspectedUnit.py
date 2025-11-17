from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, List

from CFX.Messages.Structures.TestResult import TestResult
from CFX.Messages.Structures.Inspection import Inspection
from CFX.Messages.Structures.VerificationResult import VerificationResult


@dataclass_json
@dataclass
class InspectedUnit:
    """
    Describes results of a series of inspections performed on a single production unit.
    """
    
    UnitIdentifier: str
    UnitPositionNumber: Optional[int]
    OverallResult: TestResult
    Inspections: List[Inspection]
    Verification: VerificationResult
    TotalInspectionCount: Optional[int]

    def __init__(self, unit_identifier: str = "", unit_position_number: Optional[int] = None, 
                 overall_result: TestResult = None, inspections: List[Inspection] = None, 
                 verification: VerificationResult = None, total_inspection_count: Optional[int] = None):
        """
        Default constructor
        """
        self.UnitIdentifier = unit_identifier
        self.UnitPositionNumber = unit_position_number
        self.OverallResult = overall_result or TestResult.Passed
        self.Inspections = inspections or []
        self.Verification = verification or VerificationResult.NotVerifiedYet
        self.TotalInspectionCount = total_inspection_count
