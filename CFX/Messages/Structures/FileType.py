from enum import Enum


class FileType(Enum):
    """
    Specifies the type of a file.
    """
    
    GenericMimeType = "GenericMimeType"
    DPMX = "DPMX"