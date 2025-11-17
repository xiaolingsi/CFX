from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.UnitPosition import UnitPosition


@dataclass_json
@dataclass
class UnitsUnloaded(CFXMessage):
    UniqueIdentifier: str
    Units: List[UnitPosition]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, unique_identifier: str = "", units: List[UnitPosition] = None):
        super().__init__()
        self.type = "CFX.Production.LoadingAndUnloading.UnitsUnloaded,CFX"
        self.message_name = "CFX.Production.LoadingAndUnloading.UnitsUnloaded"
        self.UniqueIdentifier = unique_identifier
        self.Units = units or []