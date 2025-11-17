from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class PackagingInfo:
    """** NOTE: ADDED in CFX 1.5 **
    Describes the packaging information of a material package.
    Abstract base class."""
    
    pass