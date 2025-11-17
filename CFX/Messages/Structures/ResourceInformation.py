from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json
from .IdentifierUniquenessType import IdentifierUniquenessType
from .MaintenanceStatus import MaintenanceStatus

@dataclass_json
@dataclass
class ResourceInformation:
    """** NOTE: ADDED in CFX 1.3 **
    Dynamic structure that contains information related to the resources / sub-resources in an Endpoint.
    It may be used to model, among the others: camera, conveyor, gantries and other 
    parts that may require traceable operations (i.e. maintenance)"""
    
    def __post_init__(self):
        if self.AdditionalSubResources is None:
            self.AdditionalSubResources = []
    
    # Name of the resource / sub-resource in the endpoint
    ResourceName: Optional[str] = None
    
    # The internal identifier (if applicable) of the part that is installed at this position.
    ResourceIdentifier: Optional[str] = None
    
    # An enumeration indicating the type of unique identifier for the specified resource
    # Values: GloballyPersistent, LocallyPersistent, UnserializedLocation or Unknown
    IdentiferUniqueness: Optional[IdentifierUniquenessType] = None
    
    # The type of the part that is installed at this position.
    ResourceType: Optional[str] = None
    
    # The position where the required part is installed on the Endpoint (optional). 
    # Where applicable, a dot (".") notation should be utilized to designate specific positions.
    # Examples: MODULE1.BEAM1.HEADPOS2, MODULE1.NEST3.NOZZLESLOT4, etc.
    ResourcePosition: Optional[str] = None
    
    # The maintenance status for this resource
    MaintenanceStatus: Optional[MaintenanceStatus] = None
    
    # Optional:In case a nonstandard additional resource shall be modelled.
    # This list gives the flexibility of modelling objects which are not explicitly specified in the model.
    # The recommendation is to use this field only in case of unknown resource types 
    AdditionalSubResources: List['ResourceInformation'] = field(default_factory=list)