from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX import CFXMessage

@dataclass_json
@dataclass
class IdentifiersNotRead(CFXMessage):
    """
    Sent by an identification device (barcode scanner, RFID reader, etc.) when the device attempts to read or interpret
    an identifier, but is unable to do so.
    """
    def __init__(self):
        super().__init__()
        self.positions_not_read: List[int] = []
        self.message_name = "CFX.Sensor.Identification.IdentifiersNotRead"

    positions_not_read: List[int]