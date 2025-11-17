from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .MaintenanceState import MaintenanceState

@dataclass_json
@dataclass
class MaintenanceStatus:
    """Maintenance status provides the information about the condition of a
    resource in a resource / machine."""
    
    # The reason why the resource should be locked in case of result state is not ok  
    Reason: Optional[str] = None
    
    # The result status of the response to the request.
    ResultState: Optional[MaintenanceState] = None