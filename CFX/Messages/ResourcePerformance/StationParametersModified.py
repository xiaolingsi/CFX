from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.GenericParameter import GenericParameter


@dataclass_json
@dataclass
class StationParametersModified(CFXMessage):
    ModifiedParameters: List[GenericParameter] = field(default_factory=list)

    def to_cfx_json(self):
        ModifiedParameters = list()
        for ele in self.ModifiedParameters:
            ModifiedParameters.append({
                "$type": "CFX.Structures.GenericParameter, CFX",
                "Name": ele.Name,
                "Value": ele.Value
            })
        StationParametersModified_json = {
            "ModifiedParameters": ModifiedParameters
        }
        return StationParametersModified_json

    def __init__(self, modified_parameters=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.StationParametersModified,CFX"
        self.message_name = "CFX.ResourcePerformance.StationParametersModified"
        self.ModifiedParameters = modified_parameters if modified_parameters is not None else []

    def add_modified_parameter(self, parameter: GenericParameter):
        self.ModifiedParameters.append(parameter)



