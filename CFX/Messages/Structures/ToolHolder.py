from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ToolHolder:
    """
    Describes a location on a process endpoint where a tool may be stored.
    """
    
    # Unique identifier of the tool holder (barcode, RFID, etc.)
    LocationUniqueIdentifier: str = ""
    
    # The name of the tool holder location
    LocationName: str = ""
    
    # If this tool holder is part of a nest or group of nozzle holders, 
    # this is the nest or group name.
    BaseName: str = ""