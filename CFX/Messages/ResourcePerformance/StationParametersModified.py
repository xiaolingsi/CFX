from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.GenericParameter import GenericParameter


class StationParametersModified(CFXMessage):
    ModifiedParameters: list

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

    def __init__(self):
        super().__init__()
        self.type = "CFX.ResourcePerformance.StationParametersModified,CFX"
        self.message_name = "CFX.ResourcePerformance.StationParametersModified"
        self.ModifiedParameters = list()

    def add_modified_parameter(self, parameter: GenericParameter):
        self.ModifiedParameters.append(parameter)



