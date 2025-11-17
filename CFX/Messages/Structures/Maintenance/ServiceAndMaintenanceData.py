from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from ..Calibration import Calibration
from .ErrorInformation import ErrorInformation
from .MaintenanceInformation import MaintenanceInformation
from .SensorInformation import SensorInformation
from .VerificationInformation import VerificationInformation


@dataclass_json
@dataclass
class ServiceAndMaintenanceData:
    """** NOTE: ADDED in CFX 1.3 **
    Dynamic structure that contains information related to the service and maintenance 
    of the resources / sub-resources in an Endpoint.
    It may be used to model as base class for other specific maintenance parts or services"""
    
    def __post_init__(self):
        if self.CalibrationDetails is None:
            self.CalibrationDetails = []
        if self.ErrorDetails is None:
            self.ErrorDetails = []
        if self.MaintenanceDetails is None:
            self.MaintenanceDetails = []
        if self.SensorDetails is None:
            self.SensorDetails = []
        if self.VerificationDetails is None:
            self.VerificationDetails = []
    
    # Unique identifier of the resource this data is about
    UniqueIdentifier: Optional[str] = None
    
    # The name of the resource this data is about
    Name: Optional[str] = None
    
    # The list of calibration details.
    CalibrationDetails: List[Calibration] = field(default_factory=list)
    
    # The list of error details.
    ErrorDetails: List[ErrorInformation] = field(default_factory=list)
    
    # The list of last executed maintenance and counters details.
    MaintenanceDetails: List[MaintenanceInformation] = field(default_factory=list)
    
    # The list of sensor details.
    SensorDetails: List[SensorInformation] = field(default_factory=list)
    
    # The list of verification details.
    VerificationDetails: List[VerificationInformation] = field(default_factory=list)