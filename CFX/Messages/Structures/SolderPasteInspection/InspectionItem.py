"""
** NOTE: ADDED in CFX 1.3 **
Provide information of the object to be inspected
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional
from .InspectionItemType import InspectionItemType
from .InspectionStep import InspectionStep


@dataclass_json
@dataclass
class InspectionItem:
    """
    ** NOTE: ADDED in CFX 1.3 **
    Provide information of the object to be inspected
    """
    
    # An optional field to specify the classification, like "Capacitor", "Resistor", "DPAK"
    Group: Optional[str] = None
    
    # Inspection object type enumeration 
    Type: Optional[InspectionItemType] = None
    
    # Unique Number of the inspection object, The No will be used in the Unit inspection messages to uniquely identify the Inspection step
    # Its unique within this recipe
    RefNo: int = 0
    
    # An optional designators (instances of a part) on a production unit(s)
    # May include sub-components in "." notation.  Examples:  R1, R2, R3   or  R2.3 (R2, pin 3)
    CRD: Optional[str] = None
    
    # Optional: The part number (internal) of the assembly to be produced by this Work Order.
    PartNumber: Optional[str] = None
    
    # When available, it describes the shape of the inspected object.
    # For example, if the object is a component (0201, 0402 etc.)
    PackageType: Optional[str] = None
    
    # Each Inspection is to be inspected applying one or more inspection steps
    # Each inspection step is associated with a measurement
    Steps: List[InspectionStep] = field(default_factory=list)