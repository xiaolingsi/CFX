from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json
from .Test import Test
from .TestResult import TestResult


@dataclass_json
@dataclass
class TestedUnit:
    """
    A data structure that represents a unit under test
    """
    
    # Unique ID of Production Unit, Panel, or Carrier
    UnitIdentifier: str = ""
    
    # Logical reference of production unit as defined by CFX position rule (see CFX standard section 5.6). 
    UnitPositionNumber: Optional[int] = 0
    
    # An enumeration indicating the overall result of the testing that was done to this unit
    OverallResult: TestResult = TestResult.Passed
    
    # A list of tests that were performed on this unit
    Tests: List[Test] = field(default_factory=list)