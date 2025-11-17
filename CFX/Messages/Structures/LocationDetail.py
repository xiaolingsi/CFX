from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class LocationDetail:
    """
    Describes detailed information about a particular location. This is a dynamic structure.
    """
    
    LocationIdentifier: Optional[str] = None
    LocationName: Optional[str] = None

    def __init__(self, locationIdentifier=None, LocationName=None):
        self.LocationIdentifier = LocationIdentifier
        self.LocationName = LocationName