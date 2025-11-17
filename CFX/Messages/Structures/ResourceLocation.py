from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from dataclasses_json import dataclass_json
from .Resource import Resource
from .LocationDetail import LocationDetail

if TYPE_CHECKING:
    from typing import Self


@dataclass_json
@dataclass
class ResourceLocation:
    """** NOTE: ADDED in CFX 1.7 **
    Describes a resource location"""
    
    # The Resource on which is material is located (optional)
    # If null, it is assumed that is Resource is the one associated to the source Endpoint of the message
    Resource: Optional[Resource] = None
    
    # Optional details on the location. Ignored if set to null.
    # This is a dynamic structure.
    LocationDetail: Optional[LocationDetail] = None
    
    # An upper level ResourceLocation in which this ResourceLocation is located (optional)
    ParentResourceLocation: Optional['Self'] = None

    def __init__(self, resource=None, location_detail=None, parent_resource_location=None):
        self.Resource = resource
        self.LocationDetail = location_detail
        self.ParentResourceLocation = parent_resource_location