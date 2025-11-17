from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from dataclasses_json import dataclass_json
from .Symptom import Symptom
from .Defect import Defect
from .Measurement import Measurement
from .EnvironmentalCondition import EnvironmentalCondition
from .TestResult import TestResult
from ...CFXUtils import CFXUtils


@dataclass_json
@dataclass
class Test:
    """
    Describes a single test in a series of test that an tester makes (both human or automation)
    in the course of testing a production unit.
    """
    
    # A unique indentifier describing a particular instance of a test that was undertaken.
    # Each new occurrence or recurrence of this same inspection gets a new unique identifier.
    UniqueIdentifier: str = ""
    
    # Identifies the nature of the test performed
    TestName: str = ""
    
    # Indicates the time when this particular test began (if known)
    TestStartTime: Optional[datetime] = CFXUtils.get_iso8601_time()
    
    # Indicates the time when this particular test ended (if known)
    TestEndTime: Optional[datetime] = CFXUtils.get_iso8601_time()
    
    # A list of environmental conditions (temperature, humidity, etc.) which
    # were in place when the test was performed.
    TestConditions: List[EnvironmentalCondition] = field(default_factory=list)
    
    # Procedure to be followed to perform this test (primarily for human driven test).
    TestProcedure: str = ""
    
    # Optional comments from the tester who tested the unit
    Comments: str = ""
    
    # The overall result of the test
    Result: TestResult = TestResult.Passed
    
    # In the case that the test cannot be completed, the error that was the cause of this outcome.
    Error: str = ""
    
    # The symptoms that were discovered in the course of this test
    SymptomsFound: List[Symptom] = field(default_factory=list)
    
    # The defects that were discovered in the course of this test
    DefectsFound: List[Defect] = field(default_factory=list)
    
    # The measurements that were taken in the course of performing this test.
    # NOTE - Only measurements not related to particular defects or symptoms should be recorded here.
    Measurements: List[Measurement] = field(default_factory=list)