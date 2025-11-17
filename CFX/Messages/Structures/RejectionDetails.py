from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RejectionDetails:
    """Describes details on a rejection of a component"""
    
    pass