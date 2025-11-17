from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ToolSetupRequirement:
    """
    Describes a single, specific tool that must be setup a particular process endpoint to execute
    a particular process.  Includes the part number of the tool, along with the 
    specific location where the tool loaded (when applicable).
    """
    
    # The position where the required tool must be installed on the Endpoint (optional).  
    # Where applicable, a dot (".") notation should be utilized to designate 
    # specific positions.  Examples:  MODULE1.BEAM1.HEADPOS2, MODULE1.NEST3.NOZZLESLOT4, etc.
    Position: Optional[str] = None
    
    # The internal part number of the tool that must be loaded at this position.
    PartNumber: str = ""
    
    # Optional.  If a very specific tool is required (specific serial number), the unique identifier
    # of that specific tool will be provided by this property.  If any tool of a certain part number
    # may be user, this property will be null.
    ToolIdentifier: Optional[str] = None