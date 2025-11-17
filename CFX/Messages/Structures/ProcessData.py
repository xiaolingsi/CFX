from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class ProcessData:
    """Dynamic data structure representing data that was collected during the processing of a production unit or collection of units."""
    
    pass