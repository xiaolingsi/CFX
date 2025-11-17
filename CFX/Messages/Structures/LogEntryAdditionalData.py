from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class LogEntryAdditionalData(object):
    """
    A dynamic structure describing additional data for the LogEntryRecorded message
    """
    
    pass