from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .WorkOrderIdentifier import WorkOrderIdentifier


@dataclass_json
@dataclass
class ScheduledWorkOrderIdentifier:
    """
    Data structure which identifies a Work Order that has already been scheduled for production.
    """
    
    # Identifies the Work Order (or Work Order sub-batch) that is scheduled.
    WorkOrderIdentifier: WorkOrderIdentifier = field(default_factory=WorkOrderIdentifier)
    
    # Identifies the physical location where the Work Order will be executed.  A single Work Order
    # may be scheduled to run in different physical locations at different times.
    WorkArea: str = ""