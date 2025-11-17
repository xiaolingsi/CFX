from enum import Enum


class FileTransferDirection(Enum):
    """
    Specifies the mode of file transfer.
    """
    
    Push = "Push"
    Pull = "Pull"