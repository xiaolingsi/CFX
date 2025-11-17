from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.UnitInfo import UnitInfo


@dataclass_json
@dataclass
class GetUnitInfoResponse(CFXMessage):
    Result: RequestResult
    PrimaryIdentifier: str
    HermesIdentifier: str
    UnitCount: int
    Units: List[UnitInfo]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, primary_identifier: str = "", hermes_identifier: str = "", units: List[UnitInfo] = None):
        super().__init__()
        self.type = "CFX.Production.GetUnitInfoResponse,CFX"
        self.message_name = "CFX.Production.GetUnitInfoResponse"
        self.Result = result or RequestResult()
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.UnitCount = len(units) if units else 0
        self.Units = units or []