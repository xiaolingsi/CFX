import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Fault import Fault
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.GenericParameter import GenericParameter
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class ModifyStationParametersRequest(CFXMessage):
    NewParameters:list

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self):
        super().__init__()
        self.type = "CFX.ResourcePerformance.ModifyStationParametersRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.ModifyStationParametersRequest"
        self.NewParameters = []

    def add_parameter(self,genericParameter:GenericParameter):
        self.NewParameters.append(genericParameter)


