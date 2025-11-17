from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ProcessData import ProcessData
from CFX.Messages.Structures.Cleaning.CleaningReading import CleaningReading


@dataclass_json
@dataclass
class CleaningManagementData(ProcessData):
    """
    Data for dome legacy cleaning equipment, which cannot be equipped with a messaging interface.
    However, such equipment can be extended with a stand-alone Cleaning Agent Concentration Management System 
    to take care of controlling and monitoring of the cleaning liquids.
    NOTE: ADDED in CFX 1.5
    """
    
    # A list of readings / measurements that have been taken for this cleaning step
    Readings: List[CleaningReading] = field(default_factory=list)
    
    def __init__(self, readings=None):
        super().__init__()
        self.Readings = readings if readings is not None else []