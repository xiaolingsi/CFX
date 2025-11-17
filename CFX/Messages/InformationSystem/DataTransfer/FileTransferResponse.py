from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.File import File
from CFX.Messages.Structures.FileTransferMode import FileTransferMode


@dataclass_json
@dataclass
class FileTransferResponse(CFXMessage):
    Result: RequestResult
    FileTitle: str
    FileLocation: str
    TransferMode: FileTransferMode
    File: File

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, file_title: str = "", 
                 file_location: str = "", transfer_mode: FileTransferMode = None, 
                 file: File = None):
        super().__init__()
        self.type = "CFX.InformationSystem.DataTransfer.FileTransferResponse,CFX"
        self.message_name = "CFX.InformationSystem.DataTransfer.FileTransferResponse"
        self.Result = result
        self.FileTitle = file_title
        self.FileLocation = file_location
        self.TransferMode = transfer_mode
        self.File = file