from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class GetMagazineDataRequest(CFXMessage):
    MagazineId: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, magazine_id: str = ""):
        super().__init__()
        self.type = "CFX.Production.Hermes.GetMagazineDataRequest,CFX"
        self.message_name = "CFX.Production.Hermes.GetMagazineDataRequest"
        self.MagazineId = magazine_id