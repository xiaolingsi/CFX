from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.Magazine import Magazine


@dataclass_json
@dataclass
class GetMagazineDataResponse(CFXMessage):
    Result: RequestResult
    MagazineData: Magazine

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, magazine_data: Magazine = None):
        super().__init__()
        self.type = "CFX.Production.Hermes.GetMagazineDataResponse,CFX"
        self.message_name = "CFX.Production.Hermes.GetMagazineDataResponse"
        self.Result = result or RequestResult()
        self.MagazineData = magazine_data or Magazine()