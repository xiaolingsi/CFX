from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.LogImportance import LogImportance
from CFX.Messages.UnitPojo.Stage import Stage

@dataclass_json
@dataclass
class LogEntryRecorded(CFXMessage):
    Importance:LogImportance
    InformationId:str
    Lane:int
    Message:str
    Stage:Stage


    def to_cfx_json(self):
        return self.to_json()

    def __init__(self,information_id,message):
        super().__init__()
        self.type = "CFX.ResourcePerformance.LogEntryRecorded,CFX"
        self.message_name = "CFX.ResourcePerformance.LogEntryRecorded"
        self.Stage = None
        self.Importance = LogImportance.Information
        self.InformationId = information_id
        self.Lane = 0
        self.Message = message


if __name__ == '__main__':
    logEntryRecorded = LogEntryRecorded("information_id","hah")
    print(logEntryRecorded.to_cfx_json())