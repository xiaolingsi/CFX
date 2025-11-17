from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitInfo import UnitInfo


@dataclass_json
@dataclass
class GetInspectionInfoRequest(CFXMessage):
    PrimaryIdentifier: str
    HermesIdentifier: str
    Units: List[UnitInfo]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, primary_identifier: str = "", hermes_identifier: str = "", units: List[UnitInfo] = None):
        super().__init__()
        self.type = "CFX.Production.TestAndInspection.GetInspectionInfoRequest,CFX"
        self.message_name = "CFX.Production.TestAndInspection.GetInspectionInfoRequest"
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.Units = units or []