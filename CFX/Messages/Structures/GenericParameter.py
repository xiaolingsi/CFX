import json

from CFX.Messages.Structures.Paramter import Parameter
from dataclasses import dataclass
from dataclasses_json import dataclass_json


class GenericParameter(Parameter):
    Name: str
    Value: str

    def to_json(self):
        return {
            "$type": "CFX.Structures.GenericParameter, CFX",
            "Name": self.Name,
            "Value": self.Value
        }

    def __init__(self, name, value):
        self.Name = name
        self.Value = value
