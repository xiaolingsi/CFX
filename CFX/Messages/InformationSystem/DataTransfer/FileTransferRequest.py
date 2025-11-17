from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.File import File
from CFX.Messages.Structures.FileTransferDirection import FileTransferDirection
from CFX.Messages.Structures.FileTransferMode import FileTransferMode


@dataclass_json
@dataclass
class FileTransferRequest(CFXMessage):
    FileTitle: str
    FileLocation: str
    TransferDirection: FileTransferDirection
    TransferMode: FileTransferMode
    File: File

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, file_title: str = "", file_location: str = "", 
                 transfer_direction: FileTransferDirection = None, 
                 transfer_mode: FileTransferMode = None, file: File = None):
        super().__init__()
        self.type = "CFX.InformationSystem.DataTransfer.FileTransferRequest,CFX"
        self.message_name = "CFX.InformationSystem.DataTransfer.FileTransferRequest"
        self.FileTitle = file_title
        self.FileLocation = file_location
        self.TransferDirection = transfer_direction
        self.TransferMode = transfer_mode
        self.File = file