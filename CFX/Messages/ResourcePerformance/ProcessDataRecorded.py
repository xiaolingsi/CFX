from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ProcessData import ProcessData


@dataclass_json
@dataclass
class ProcessDataRecorded(CFXMessage):
    """
    Cleaning Agent needs to report the status of the cleaning liquid regularly.
    ** NOTE: ADDED in CFX 1.5 **
    """
    process_data: ProcessData = field(default_factory=ProcessData)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, process_data=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.ProcessDataRecorded,CFX"
        self.message_name = "CFX.ResourcePerformance.ProcessDataRecorded"
        self.process_data = process_data if process_data is not None else ProcessData()