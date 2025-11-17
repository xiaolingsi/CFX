from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from CFX.Messages.Structures.FileType import FileType


@dataclass_json
@dataclass
class File(object):
    """
    A data structure that represents a data file of any type.
    The file may be of a known MIME type, or a specialized type defined by CFX.
    """
    
    FileType: Optional[FileType] = None
    MimeType: Optional[str] = None
    FileData: Optional[bytes] = None
    FileURL: Optional[str] = None

    def __init__(self):
        pass