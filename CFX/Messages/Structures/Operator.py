from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from .ActorType import ActorType

@dataclass_json
@dataclass
class Operator:
    """Represents an operator who performs a function"""
    
    # An optional unique identifier for the Operator
    OperatorIdentifier: Optional[str] = None
    
    # The nature of operator
    ActorType: ActorType = field(default_factory=lambda: ActorType.Human)
    
    # The Family Name of Operator
    LastName: Optional[str] = None
    
    # The Given Name of Operator
    FirstName: Optional[str] = None
    
    # The Login Name for this Operator
    LoginName: Optional[str] = None

    def __init__(self, operator_identifier=None, actor_type=None, last_name=None, 
                 first_name=None, login_name=None):
        self.OperatorIdentifier = operator_identifier
        self.ActorType = actor_type if actor_type is not None else ActorType.Human
        self.LastName = last_name
        self.FirstName = first_name
        self.LoginName = login_name