import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.TestedUnit import TestedUnit
from CFX.Messages.Structures.TestMethod import TestMethod
from CFX.Messages.Structures.SamplingInformation import SamplingInformation


@dataclass_json
@dataclass
class UnitsTested(CFXMessage):
    TransactionId: str
    TestMethod: TestMethod
    Tester: Operator
    SamplingInformation: SamplingInformation
    TestedUnits: List[TestedUnit]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transaction_id: str = "", test_method: TestMethod = "",
                 tester: Operator = None, sampling_information: SamplingInformation = None, 
                 tested_units: List[TestedUnit] = None):
        super().__init__()
        self.type = "CFX.Production.TestAndInspection.UnitsTested,CFX"
        self.message_name = "CFX.Production.TestAndInspection.UnitsTested"
        self.TransactionId = transaction_id or uuid.uuid4()
        self.TestMethod = TestMethod.Human
        self.Tester = tester or Operator()
        self.SamplingInformation = sampling_information or SamplingInformation()
        self.TestedUnits = tested_units or []