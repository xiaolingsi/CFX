from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import datetime
from .CounterType import CounterType

@dataclass_json
@dataclass
class MaintenanceInformation:
    """** NOTE: ADDED in CFX 1.3 **
    Dynamic structure that contains information related to the counters of the 
    resources / sub-resources in an Endpoint. It is the information that allows the
    receiving system to plan / execute the maintenance operations"""
    
    # The user friendly name of counter data source.
    Name: Optional[str] = None
    
    # The type of the counter for this element.
    CounterType: Optional[CounterType] = None
    
    # Optional field. 
    # When CounterType = NonStandard, this field allows the sender to specify a custom counter
    CustomCounterType: Optional[str] = None
    
    # The location of the data source providing the counter information (optional, only if available).
    # It may be used to distinguish, for example, the counters of multi-lane feeder
    # Where applicable, a dot (".") notation should be utilized to designate specific positions.
    # Examples: MODULE1.BEAM1.HEADPOS2, MODULE1.NEST3.NOZZLESLOT4, etc.
    MeasurementLocation: Optional[str] = None
    
    # The current value of the counter.
    CurrentCounterValue: Optional[float] = None
    
    # The current maintenance ratio at reading time. This value is close to 0 for 
    # recent executed maintenance and close to 100 for parts requiring maintenance.
    # NOTE: this value may be also more than 100
    CurrentRatio: Optional[float] = None
    
    # Provides additional information on the lifetime usage of this part. 
    # It is "false" for parts which do not own an independent maintenance cycle.
    # Instead, the maintenance is done as part of a higher level resource 
    # (for example the maintenance of rotation-axis, star axis, and z axis are part of head maintenance) or not at all
    CurrentRatioValid: Optional[bool] = None
    
    # Timestamp when the maintenance counter was sampled. 
    CurrentTimeStamp: Optional[datetime] = None
    
    # The value of the counter during the last maintenance
    LastMaintenanceCounterValue: Optional[float] = None
    
    # Timestamp when the last maintenance was done. 
    LastMaintenanceTimeStamp: Optional[datetime] = None
    
    # It is true, if at least one maintenance was succesfully done.
    # If false, both LastMaintenanceCounterValue and LastMaintenanceTimeStamp are invalid and cannot be used. 
    LastMaintenanceValid: Optional[bool] = None