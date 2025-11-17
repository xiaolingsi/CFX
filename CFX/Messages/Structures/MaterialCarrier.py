from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from dataclasses_json import dataclass_json

if TYPE_CHECKING:
    from typing import Self


@dataclass_json
@dataclass
class MaterialCarrier:
    """A dynamic structure which describes a device that is mounted at a process endpoint which contains
    source materials that are then consumed by the endpoint.  An SMD Tape Feeder would be an example of a MaterialCarrier.
    This base MaterialCarrier structure is used to describe a generic carrier, when a more specific carrier location class is
    not available, such as SMDTapeFeeder, SMDTubeFeeder, and SMDTubeFeeder."""
    
    # The unique identifier for this carrier (barcode, RFID, etc.)
    UniqueIdentifier: Optional[str] = None
    
    # A human readable name for this carrier
    Name: Optional[str] = None
    
    # ** NOTE: ADDED in CFX 1.6 **
    # An upper level carrier in which this carrier is loaded (optional)
    ParentCarrier: Optional['Self'] = None

    def __init__(self, unique_identifier=None, name=None, parent_carrier=None):
        self.UniqueIdentifier = unique_identifier
        self.Name = name
        self.ParentCarrier = parent_carrier