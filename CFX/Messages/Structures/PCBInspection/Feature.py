from dataclasses import dataclass, field
from typing import Optional, List, Union
from dataclasses_json import dataclass_json, config
from ..NamedObject import NamedObject

@dataclass_json
@dataclass
class Feature(NamedObject):
    """A feature/charcteristic/property/attribute (of a panel, board, componemnt, etc.) to check."""
    
    def __post_init__(self):
        if self.Values is None:
            self.Values = []
    
    # This feature was checked.
    # (The inspection may have been skipped due to a defect detected earlier, so further
    # time consuming inspections are pointless.)
    IsInspected: Optional[bool] = None
    
    # The inspection has detected/classified this feature as defect.
    IsDetectedDefect: bool = False
    
    # This (usually defective) feature was verified (AKA "classified") by a human.
    IsVerified: bool = False
    
    # The verification (AKA "classification") by a human has confirmed a defect.
    IsVerifiedDefect: bool = False
    
    # The (eventual) defect was repaired successfully.
    IsRepaired: bool = False
    
    # List of values (of varying types).
    Values: List['Feature.Value'] = field(default_factory=list)
    
    @property
    def IsDefect(self) -> bool:
        """The feature is out of its allowed limits, so it is assumed to be a defect.
        But a defect detected during inspection may have been identified as a "false call" in verification
        or may have been repaired.
        """
        if self.IsRepaired:
            return False  # Feature was repaired successfully, so not a defect anymore.
        
        if self.IsVerified:               # The verification (by a human) has
            return self.IsVerifiedDefect  # either confirmed the defect or has corrected the inspection result (i.e. it was a "false call").
        
        if self.IsInspected is not None and not self.IsInspected:
            return True   # This feature was not inspected/checked at all, as a precaution it is rated like a defect.
        
        return self.IsDetectedDefect   # The (automatic) inspection may have detected a defect.


@dataclass_json
@dataclass
class Value(NamedObject):
    """Base class for feature values."""
    
    # The name of the unit for this value.
    Unit: Optional[str] = None


@dataclass_json
@dataclass
class StringValue(Value):
    """Representation of a string value."""
    
    # A string value.
    Value: Optional[str] = None


@dataclass_json
@dataclass
class FloatValue(Value):
    """Representation of a float value."""
    
    # A float value.
    Value: Optional[float] = None


@dataclass_json
@dataclass
class IntValue(Value):
    """Representation of an integer value."""
    
    # An integer value.
    Value: Optional[int] = None