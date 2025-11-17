from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import datetime
from .NonInstalledComponentLocation import NonInstalledComponentLocation
from .Stage import Stage
from .RejectionReason import RejectionReason
from .RejectionDetails import RejectionDetails

@dataclass_json
@dataclass
class NonInstalledComponent:
    """Describes a particular location on a production unit where materials / parts were not installed."""
    
    def __init__(self, setDateTime: bool = False):
        if setDateTime:
            self.NonInstallationTime = datetime.now()
    
    # Location on production unit where material / parts were installed
    ReferenceDesignator: Optional[str] = None
    
    # The specific time when this material / part was tried to be installed on the production unit (optional, when known)
    NonInstallationTime: Optional[datetime] = None
    
    # The final location of the component that has not been installed
    Location: Optional[NonInstalledComponentLocation] = None
    
    # ** NOTE: ADDED in CFX 1.3 **
    # The stage name or number
    Stage: Optional[Stage] = None
    
    # Id of the rejection box where the component has been rejected (if applicable)
    RejectionBoxId: Optional[str] = None
    
    # A comment on the rejection
    RejectionComment: Optional[str] = None
    
    # The reason of the rejection of this component (Unknown if not known)
    RejectionReason: Optional[RejectionReason] = None
    
    # The rejection details, depending on the rejection reason (optional)
    RejectionDetails: Optional[RejectionDetails] = None