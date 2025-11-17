from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from .SamplingMethod import SamplingMethod


@dataclass_json
@dataclass
class SamplingInformation:
    """
    Describes the sampling strategy to be employed on a particular lot of material / units during test or inspection
    """
    
    # An enumeration describing the sampling method that was employed (if any)
    SamplingMethod: SamplingMethod = field(default=SamplingMethod.NoSampling)
    
    # The total number of units in the lot
    LotSize: Optional[float] = 0.0
    
    # The number of units from the total lot to be inspected / tested.  
    # This is a subset of the total lot.
    SampleSize: Optional[float] = 0.0