from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition
from CFX.Messages.Structures.DisqualificationReason import DisqualificationReason


@dataclass_json
@dataclass
class UnitsDisqualified(CFXMessage):
    PrimaryIdentifier: str
    HermesIdentifier: str
    Reason: DisqualificationReason
    Comments: str
    Units: List[UnitPosition]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, primary_identifier: str = "", hermes_identifier: str = "", reason: DisqualificationReason = None, 
                 comments: str = "", units: List[UnitPosition] = None):
        super().__init__()
        self.type = "CFX.Production.UnitsDisqualified,CFX"
        self.message_name = "CFX.Production.UnitsDisqualified"
        self.PrimaryIdentifier = primary_identifier
        self.HermesIdentifier = hermes_identifier
        self.Reason = reason or DisqualificationReason.DefectiveMaterials
        self.Comments = comments
        self.Units = units or []