from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.GenericParameter import GenericParameter


@dataclass_json
@dataclass
class ModifyStationParametersRequest(CFXMessage):
    NewParameters: List[GenericParameter] = field(default_factory=list)

    def to_cfx_json(self):
        parameters = []
        for ele in self.NewParameters:
            parameters.append(ele.to_json())
        return {
            "NewParameters": parameters
        }

    def __init__(self, new_parameters=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.ModifyStationParametersRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.ModifyStationParametersRequest"
        self.NewParameters = new_parameters if new_parameters is not None else []

    def add_parameter(self, genericParameter: GenericParameter):
        self.NewParameters.append(genericParameter)
