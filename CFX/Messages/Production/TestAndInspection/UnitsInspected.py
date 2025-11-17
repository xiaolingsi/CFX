import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.InspectedUnit import InspectedUnit
from CFX.Messages.Structures.SamplingInformation import SamplingInformation
from CFX.Messages.Structures.InspectionMethod import InspectionMethod


@dataclass_json
@dataclass
class UnitsInspected(CFXMessage):
    TransactionId: str
    InspectionMethod: InspectionMethod
    SamplingInformation: SamplingInformation
    Inspector: Operator
    InspectedUnits: List[InspectedUnit]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", inspection_method: str = "", 
                 sampling_information: SamplingInformation = None, inspector: Operator = None, 
                 inspected_units: List[InspectedUnit] = None):
        super().__init__()
        self.type = "CFX.Production.TestAndInspection.UnitsInspected,CFX"
        self.message_name = "CFX.Production.TestAndInspection.UnitsInspected"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.InspectionMethod = InspectionMethod.Human
        self.SamplingInformation = sampling_information or SamplingInformation()
        self.Inspector = inspector or Operator()
        self.InspectedUnits = inspected_units or []