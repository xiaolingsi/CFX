from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from datetime import datetime
from .TestResult import TestResult
from .ComponentDesignator import ComponentDesignator
from .DataType import DataType
from ...CFXUtils import CFXUtils


@dataclass_json
@dataclass
class Reading:
    """A data structure that represents a reading that was taken against a production unit or piece of equipment"""
    
    def __post_init__(self):
        if self.Components is None:
            self.Components = []
    
    # A name that uniquely describes the test or measurement that was performed.
    ReadingIdentifier: Optional[str] = None
    
    # The date/time when this Reading was recorded.
    TimeRecorded: Optional[datetime] = CFXUtils.get_iso8601_time()
    
    # An optional positive integer describing the sequence in which the tests or measurements were performed
    # that resulted in this Reading.
    ReadingSequence: int = 0
    
    # An enumeration indicating whether or not this reading is considered acceptable.
    Result: Optional[TestResult] = TestResult.Passed
    
    # In the case that this Reading is associated to a particular production unit, and the Reading is not associated
    # with a work transaction, this property contains the unique identifier of the production unit.
    UnitIdentifier: Optional[str] = None
    
    # In the case that this Reading is associated with a particular production unit, and the Reading is associated
    # with a work transaction, this property contains the position number of the unit as it relates to the transaction.  
    # If a position number is not specified, it is assumed that the Reading applies to all units associated with the
    # transaction.
    UnitPositionNumber: Optional[int] = 0
    
    # An optional list of components (instance of a part) on a production unit(s) to be associated with this reading.
    Components: List[ComponentDesignator] = field(default_factory=list)
    
    # An enumeration describing the type of value contained in the Value or BinaryValue properties.
    ValueDataType: Optional[DataType] = DataType.String
    
    # The units of the value (must be a valid SI unit)
    ValueUnits: Optional[str] = None
    
    # If the Reading is of type DataType.Binary, this property contains the MIME type
    # of the binary data contained in the BinaryValue property.
    ValueMimeType: Optional[str] = None
    
    # The value of the reading
    Value: Optional[str] = None
    
    # If the Reading is of type DataType.Binary, this property contains the binary
    # representation of the value.
    BinaryValue: Optional[bytes] = None
    
    # The expected value
    ExpectedValue: Optional[str] = None
    
    # The units of the expected value (must be a valid SI unit)
    ExpectedValueUnits: Optional[str] = None
    
    # The minimum acceptable value
    MinimumAcceptableValue: Optional[str] = None
    
    # The maximum acceptable value
    MaximumAcceptableValue: Optional[str] = None