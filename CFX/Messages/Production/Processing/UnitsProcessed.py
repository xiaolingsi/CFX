import json
import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.ProcessingResult import ProcessingResult
from CFX.Messages.Structures.ProcessData import ProcessData
from CFX.Messages.Structures.ProcessedUnit import ProcessedUnit


@dataclass_json
@dataclass
class UnitsProcessed(CFXMessage):
    TransactionId: uuid.UUID
    OverallResult: ProcessingResult
    CommonProcessData: ProcessData
    UnitProcessData: List[ProcessedUnit]

    def to_cfx_json(self):
        temp_json_dict = json.loads(self.to_json())
        res_dict = dict()
        if self.CommonProcessData and "type" in self.CommonProcessData.__dict__:
            res_dict['$type'] = self.CommonProcessData.type
        for key,value in temp_json_dict['CommonProcessData'].items():
            if key != 'type' and key != '$type':
                res_dict[key] = value
        temp_json_dict['CommonProcessData'] = res_dict
        return json.dumps(temp_json_dict, indent=2)

    def __init__(self, transaction_id: uuid.UUID = None, overall_result: ProcessingResult = ProcessingResult.Succeeded, 
                 common_process_data: ProcessData = None, unit_process_data: List[ProcessedUnit] = None):
        super().__init__()
        self.type = "CFX.Production.Processing.UnitsProcessed,CFX"
        self.message_name = "CFX.Production.Processing.UnitsProcessed"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.OverallResult = overall_result
        self.CommonProcessData = common_process_data
        self.UnitProcessData = unit_process_data or []

