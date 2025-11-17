from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import datetime
import uuid
from .TestResult import TestResult
from ...CFXUtils import CFXUtils


@dataclass_json
@dataclass
class Measurement:
    """Abstract base class for dynamic data structure which describes a measurement that was made by a human
    or by automated equipment in the course of inspecting or testing a production unit"""
    
    def __init__(self):
        self.UniqueIdentifier = str(uuid.uuid4())
    
    # A unique identifier that for this particular measurement instance
    # (new and unique each time a new measurement is made or repeated).
    UniqueIdentifier: Optional[str] = None
    
    # A name that uniquely describes the test or measurement that was performed.
    MeasurementName: Optional[str] = None
    
    # The date/time when this Measurement was recorded (if known, otherwise null)
    TimeRecorded: Optional[datetime] = CFXUtils.get_iso8601_time()
    
    # An optional positive integer describing the sequence in which the tests or measurements were performed
    # that resulted in this Reading.
    Sequence: int = 0
    
    # An enumeration indicating whether or not this measurement is considered acceptable.
    Result: Optional[TestResult] = TestResult.Passed
    
    # An optional list of component designators (instances of a part) on a production unit(s) to be associated with this measurement.
    # May include sub-components in "." notation.  Examples:  R1, R2, R3   or  R2.3 (R2, pin 3)
    CRDs: Optional[str] = None