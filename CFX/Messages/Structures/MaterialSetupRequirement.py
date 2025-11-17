from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class MaterialSetupRequirement:
    """Describes a single, specific material setup requirement at a particular process endpoint.
    Includes the material / part that must be loaded at the endpoint, along with the 
    specific location where the material must be loaded (where applicable), valid alternate
    part numbers that may be substituted for the primary part, and any applicable
    AML (Approved Manufacturer List) restrictions."""
    
    def __post_init__(self):
        if self.ApprovedAlternateParts is None:
            self.ApprovedAlternateParts = []
        if self.ApprovedManufacturerParts is None:
            self.ApprovedManufacturerParts = []
    
    # The position where the required material must be installed on the Endpoint (optional).  
    # Where applicable, a dot (".") notation should be utilized to designate 
    # specific positions.  Examples:  MODULE1.FRONT.Pos23, STAGE2.BANK1.Pos44, etc.
    Position: Optional[str] = None
    
    # The internal part number of the part that must be loaded at this position.
    PartNumber: Optional[str] = None
    
    # An optional list of approved alternate parts (internal part numbers) that may be substituted 
    # for the primary part.
    ApprovedAlternateParts: List[str] = field(default_factory=list)
    
    # An optional list of specific manufacturer part numbers that must be utilzed.  When specified,
    # a part will only be acceptable if both its internal part number matches the PartNumber property (or Alternates), 
    # AND its manufacturer part number matches one of the parts specified in the ApprovedManufacturerParts property.
    ApprovedManufacturerParts: List[str] = field(default_factory=list)