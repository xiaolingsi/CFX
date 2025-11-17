from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .ResourceInformation import ResourceInformation

@dataclass_json
@dataclass
class RotationAxes(ResourceInformation):
    """** NOTE: ADDED in CFX 1.3 **
    Rotation axis of the resource, typically the head in an Endpoint.
    It may have a meaning for the lifecycle of the resource, which may be independent
    from the Endpoint where it is located (e.g. maintenance operations)"""
    
    pass