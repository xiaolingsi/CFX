from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class Characteristic(object):
    """
    A singular characteristic that has been applied to a production unit
    """
    
    Name: Optional[str] = None
    Value: Optional[str] = None