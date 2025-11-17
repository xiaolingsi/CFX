from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from dataclasses_json import dataclass_json
from .WorkOrderIdentifier import WorkOrderIdentifier
from .WorkOrderStatus import WorkOrderStatus


@dataclass_json
@dataclass
class WorkOrder:
    """
    A structure that describes an order to produce a specifified quantity of units of a particular part number /
    part revision within the factory environment.
    """
    
    # The identifer of the Work Order or Work Order sub-batch
    WorkOrderIdentifier: WorkOrderIdentifier = field(default_factory=WorkOrderIdentifier)
    
    # A human friendly description for this Work Order.
    Description: str = ""
    
    # The current status of the Work Order.
    Status: WorkOrderStatus = WorkOrderStatus.AwaitingApproval
    
    # The name of the router or process that will be followed to produce the units for this Work Order.
    Router: str = ""
    
    # The revision of the router or process that will be followed to produce units for this Work Order.
    RouterRevision: str = ""
    
    # Ane lot number that is to be associated with units produced under this Work Order.
    LotNumber: str = ""
    
    # An optional customer name, if this Work Order is associated with particular customer.
    Customer: str = ""
    
    # An optional department name, if this Work Order is to be executed by a particular department.
    Department: str = ""
    
    # The date on which the Work Order was created.
    CreatedDate: datetime = field(default_factory=datetime.now)
    
    # The date/time on which this Work Order should begin execution.
    StartDate: datetime = field(default_factory=datetime.now)
    
    # The date/time by which this Work Order should be completed.
    DateRequired: datetime = field(default_factory=datetime.now)
    
    # The part number (internal) of the assembly to be produced by this Work Order.
    PartNumber: str = ""
    
    # The revision of the assembly to be produced by this Work Order.
    PartRevision: str = ""
    
    # The quantity of units to be produced by this Work Order.
    Quantity: float = 0.0
    
    # If the Work Order is intended to produce something other than "units", the unit of measure of the 
    # quantity associated with this Word Order.  For example, a Work Order might be placed to produce 200m
    # of red wire.  In this case, the Quantity property would be "200" and the UnitOfMeasure
    # would be "meter".  If UnitOfMeasure is left empty (blank), it is assumed that the quantity specifies
    # "pieces" and/or "units" (200 units of assembly 1234-5678, for example).
    UnitOfMeasure: str = ""
    
    # A list of other Work Orders (or Work Order sub-batches) upon which this Work Order (or Work Order sub-batch) is dependent.
    # Dependent Work Orders feed the supply of materials into upper level Work Orders.
    DependsOn: List[WorkOrderIdentifier] = field(default_factory=list)