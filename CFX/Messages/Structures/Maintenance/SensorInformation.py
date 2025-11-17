from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import datetime
from .SensorType import SensorType, SensorUnitOfMeasure
from ..ResourceInformation import ResourceInformation

@dataclass_json
@dataclass
class SensorInformation(ResourceInformation):
    """** NOTE: ADDED in CFX 1.3 **
    Dynamic structure that contains information related to the sensor of the 
    resources / sub-resources in an Endpoint.
    It may be used to model the sensor on  
    parts that may require traceable operations (i.e. maintenance)"""
    
    # The type of the sensor in this position of the resource / machine.
    Type: Optional[SensorType] = None
    
    # Optional field. 
    # When SensorType = NonStandard, this field allows the sender to specify a custom sensor
    CustomSensorType: Optional[str] = None
    
    # The value of the performed verification.
    Value: Optional[float] = None
    
    # The low limit value of the performed verification (optional)
    LowLimit: Optional[float] = None
    
    # The high limit value of the performed verification (optional)
    HighLimit: Optional[float] = None
    
    # The unit of measure of the performed sample (if applicable)
    UnitOfMeasure: Optional[SensorUnitOfMeasure] = None
    
    # Optional field. 
    # When UnitOfMeasure = NonStandard, this field allows the sender to specify a custom unit of measure
    CustomUnitOfMeasure: Optional[str] = None
    
    # The last time when the verification has been executed
    SampleTime: Optional[datetime] = None