from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Tool:
    """
    Describes a tool that is used in production
    {
        "UniqueIdentifier": "UID23890430",
        "Name": "SQUEEGEE234324"
    }
    """
    
    # The unique identifier of the Tool (barcode, RFID, etc.)
    UniqueIdentifier: str = ""
    
    # The name of the tool
    Name: str = ""