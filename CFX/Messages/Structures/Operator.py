from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ActorType import ActorType


@dataclass_json
@dataclass
class Operator(object):
    ActorType: ActorType
    FirstName: str
    LastName: str
    LoginName: str
    OperatorIdentifier: str

    def __init__(self, actor_type: ActorType = ActorType.Human,
                 first_name="",
                 last_name="",
                 login_name="",
                 operator_identifier=""):
        self.ActorType = actor_type
        self.FirstName = first_name
        self.LastName = last_name
        self.LoginName = login_name
        self.OperatorIdentifier = operator_identifier
