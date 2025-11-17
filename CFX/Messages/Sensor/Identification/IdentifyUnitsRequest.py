from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX import CFXMessage

@dataclass_json
@dataclass
class IdentifyUnitsRequest(CFXMessage):
    """
    Sent by a process endpoint to a unit identification device (such as a barcode scanner or RFID reader)
    to request the most recently scanned unit identifiers.
    """
    def __init__(self):
        super().__init__()
        self.message_name = "CFX.Sensor.Identification.IdentifyUnitsRequest"