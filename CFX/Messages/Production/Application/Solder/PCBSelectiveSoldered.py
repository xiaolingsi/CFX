import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.SolderApplication.SelectiveSolderData import SelectiveSolderData
from CFX.Messages.Structures.SolderApplication.SelectiveSolderedPCB import SelectiveSolderedPCB


@dataclass_json
@dataclass
class PCBSelectiveSoldered(CFXMessage):
    TransactionId: str
    HeaderData: SelectiveSolderData
    SolderedPCBs: List[SelectiveSolderedPCB]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", header_data: SelectiveSolderData = None, 
                 soldered_pcbs: List[SelectiveSolderedPCB] = None):
        super().__init__()
        self.type = "CFX.Production.Application.Solder.PCBSelectiveSoldered,CFX"
        self.message_name = "CFX.Production.Application.Solder.PCBSelectiveSoldered"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.HeaderData = header_data or SelectiveSolderData()
        self.SolderedPCBs = soldered_pcbs