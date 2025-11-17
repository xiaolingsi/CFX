from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from ..Resource import Resource
from ..ResourceInformation import ResourceInformation

@dataclass_json
@dataclass
class MaintenanceResource(Resource):
    """** NOTE: ADDED in CFX 1.3 **
    Describes the resources / sub-resources of a particular Endpoint that is participating in a CFX network, 
    and more specifically, is an SMT placement machine.  This is a dynamic structure."""
    
    def __post_init__(self):
        if self.Resources is None:
            self.Resources = []
    
    # Generic list for the sub-resources in this resource (machine)
    Resources: List[ResourceInformation] = field(default_factory=list)