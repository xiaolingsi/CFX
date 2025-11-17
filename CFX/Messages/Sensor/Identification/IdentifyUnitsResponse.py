from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX import CFXMessage
from CFX.Messages.Structures import UnitPosition, RequestResult

@dataclass_json
@dataclass
class IdentifyUnitsResponse(CFXMessage):
    """
    Response from a unit identification device (such as a barcode scanner or RFID reader)
    to a process endpoint which contains the most recently scanned unit identifiers.
    """
    def __init__(self):
        super().__init__()
        self.units: List[UnitPosition] = []
        self.result: RequestResult = RequestResult()
        self.message_name = "CFX.Sensor.Identification.IdentifyUnitsResponse"

    result: RequestResult
    primary_identifier: str = None
    hermes_identifier: str = None
    units: List[UnitPosition]