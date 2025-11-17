from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from dataclasses_json import dataclass_json
from .WorkOrderIdentifier import WorkOrderIdentifier
from .Operator import Operator
from .Tool import Tool
from .MaterialPackage import MaterialPackage


@dataclass_json
@dataclass
class ScheduledWorkOrder:
    """
    A data structure representing a Work Order that has been scheduled to be executed
    at a particular work area within the factory at a particular time.  Includes all of the physical 
    resources, tools, personnel, and materials that are required to execute the Work Order.
    """
    
    # Identifies the Work Order (or Work Order sub-batch) that is scheduled.
    WorkOrderIdentifier: WorkOrderIdentifier = field(default_factory=WorkOrderIdentifier)
    
    # Identifies the person who was responsible for scheduling the Work Order (optional).
    Scheduler: Optional[Operator] = None
    
    # Identifies the physical location where the Work Order will be executed.  A single Work Order
    # may be scheduled to run in different physical locations at different times.
    WorkArea: str = ""
    
    # The time when production will begin for this Work Order in the designated work area.
    StartTime: datetime = field(default_factory=datetime.now)
    
    # THe time when production is expected to be completed for this Work Order.
    EndTime: datetime = field(default_factory=datetime.now)
    
    # An optional list of the physical resources / assets that are required to 
    # execute the Work Order (Lines, Machines, etc.).
    ReservedResources: List[str] = field(default_factory=list)
    
    # An optional list of the tools that are required to execute the Work Order.
    ReservedTools: List[Tool] = field(default_factory=list)
    
    # An optional list of the operators that have been allocated to execute this scheduled
    # Work Order.
    ReservedOperators: List[Operator] = field(default_factory=list)
    
    # An optional list of the specific materials that are necessary to execute this scheduled Work Order.
    ReservedMaterials: List[MaterialPackage] = field(default_factory=list)