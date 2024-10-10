from CFX.Messages.Structures.Paramter import Parameter
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class GenericParameter(Parameter):
    Name:str
    Value:str

    def __init__(self,name,value):
        self.Name = name
        self.Value = value