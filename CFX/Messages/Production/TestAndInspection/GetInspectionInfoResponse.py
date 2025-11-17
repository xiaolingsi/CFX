from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.InspectedUnit import InspectedUnit


@dataclass_json
@dataclass
class GetInspectionInfoResponse(CFXMessage):
    InspectedUnits: List[InspectedUnit]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, inspected_units: List[InspectedUnit] = None):
        super().__init__()
        self.type = "CFX.Production.TestAndInspection.GetInspectionInfoResponse,CFX"
        self.message_name = "CFX.Production.TestAndInspection.GetInspectionInfoResponse"
        self.InspectedUnits = inspected_units or []