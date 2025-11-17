from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Magazine import Magazine


@dataclass_json
@dataclass
class MagazineArrived(CFXMessage):
    MagazineData: Magazine

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, magazine_data: Magazine = None):
        super().__init__()
        self.type = "CFX.Production.Hermes.MagazineArrived,CFX"
        self.message_name = "CFX.Production.Hermes.MagazineArrived"
        self.MagazineData = magazine_data or Magazine()