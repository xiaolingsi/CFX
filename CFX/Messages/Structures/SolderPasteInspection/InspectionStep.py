"""
** NOTE: ADDED in CFX 1.3 **
An inspection step is one step of an inspection. Each inspection step is associated with a measurements result.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from ..Measurement import Measurement


@dataclass_json
@dataclass
class InspectionStep:
    """
    ** NOTE: ADDED in CFX 1.3 **
    An inspection step is one step of an inspection. Each inspection step is associated with a measurements result.
    """
    
    # Optional: name of the inspection step
    # E.g.: This could be the name of the algorithm to be  applied to perform the inspection step
    Name: Optional[str] = None
    
    # Uniquely identifies the Inspection step for this Inspection Object
    Sequence: int = 0
    
    # the target values for the related measurement
    # In case of a SPI the InspectionMeasurementTarget would be used to provide the expected values
    TargetValue: Optional[Measurement] = None