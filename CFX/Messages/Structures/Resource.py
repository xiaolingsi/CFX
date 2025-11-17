from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from .ResourceType import ResourceType as ResourceType_

@dataclass_json
@dataclass
class Resource:
    """** NOTE: ADDED in CFX 1.3 **
    Describes details of a particular Resource.
    This is a dynamic structure."""
    
    # The barcode, RFID, or other unique identifier that is used to identify this machine / resource.
    UniqueIdentifier: Optional[str] = None
    
    # The name of the resource to be used in GUIs or reporting (optional)
    Name: Optional[str] = None
    
    # The type of resource (e.g. SMT, AOI, Oven). 
    ResourceType: Optional[str] = None
    
    # ** NOTE: ADDED in CFX 1.7 **
    # The type of resource (machine, shelf...). 
    Type: Optional[ResourceType] = field(default_factory=lambda: ResourceType_.Unknown)
    
    # The name of the vendor of the machine / resource (optional)
    Vendor: Optional[str] = None
    
    # The model number of the machine / resource
    ModelNumber: Optional[str] = None
    
    # The serial number of the machine / resource
    SerialNumber: Optional[str] = None
    
    # The software version of the machine / resource
    SoftwareVersion: Optional[str] = None
    
    # The firmware version of the machine / resource (optional)
    FirmwareVersion: Optional[str] = None

    def __init__(self, unique_identifier=None, name=None, resource_type=None, 
                 type=None, vendor=None, model_number=None, serial_number=None, 
                 software_version=None, firmware_version=None):
        self.UniqueIdentifier = unique_identifier
        self.Name = name
        self.ResourceType = resource_type
        self.Type = type if type is not None else ResourceType_.Unknown
        self.Vendor = vendor
        self.ModelNumber = model_number
        self.SerialNumber = serial_number
        self.SoftwareVersion = software_version
        self.FirmwareVersion = firmware_version