from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List, Optional
from CFX import CFXMessage
from CFX.Structures import UnitPosition

@dataclass_json
@dataclass
class IdentifiersRead(CFXMessage):
    """
    Sent by an identification device (barcode scanner, RFID reader, etc.) when the device has identified one or more items.
    """
    def __init__(self):
        super().__init__()
        self.message_name = "CFX.Sensor.Identification.IdentifiersRead"

    primary_identifier: Optional[str] = None
    hermes_identifier: Optional[str] = None
    units: Optional[List[UnitPosition]] = None