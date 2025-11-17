from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class GetUnitInfoRequest(CFXMessage):
    PrimaryIdentifier: str
    HermesIdentifier: str
    UnitIdentifier: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, primary_identifier: str = "", hermes_identifier: str = "", unit_identifier: str = ""):
        super().__init__()
        self.type = "CFX.Production.GetUnitInfoRequest,CFX"
        self.message_name = "CFX.Production.GetUnitInfoRequest"
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.UnitIdentifier = unit_identifier