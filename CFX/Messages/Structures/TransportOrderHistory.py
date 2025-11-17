from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from dataclasses_json import dataclass_json
from .TransportOrderStatus import TransportOrderStatus
from .Operator import Operator


@dataclass_json
@dataclass
class TransportOrderHistory:
    """
    Describes a single event in the history of a transport order.  
    A transport order is a directive to move materials / WIP / production
    units from one location to another.
    """
    
    # The date and time when the event took place.  If null, this implies
    # that the date and time provided by the parent message should be applied
    # to this event.
    EventDateTime: Optional[datetime] = None
    
    # The status of this transport order at the time of the event
    Status: TransportOrderStatus = TransportOrderStatus.Unspecified
    
    # The operator involved in this event (optional, where applicable)
    Operator: Optional[Operator] = None
    
    # The location where this event took place
    Location: str = ""
    
    # Human readable comments related to this event (where applicable)
    Comments: str = ""