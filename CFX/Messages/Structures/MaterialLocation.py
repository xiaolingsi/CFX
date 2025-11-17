from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from .MaterialPackage import MaterialPackage
from .MaterialCarrier import MaterialCarrier
from .ResourceLocation import ResourceLocation

@dataclass_json
@dataclass
class MaterialLocation:
    """Describes a specific location on an endpoint where material may be loaded.
    Also includes information about the current contents of this location (if applicable)."""
    
    # ** NOTE: ADDED in CFX 1.7 **
    # The ResourceLocation on which the material is located (optional)
    # If null, it is assumed that the Resource is the one associated to the source Endpoint
    ResourceLocation: Optional[ResourceLocation] = None
    
    # The unique identifier (barcode) of the location on the Endpoint / Resource where the MaterialPackage is to be loaded.
    # If this property is left empty, the MaterialPackage will only be loaded to the carrier specified
    # by the CarrierInformation property, and not to an Endpoint / Resource.
    LocationIdentifier: Optional[str] = None
    
    # Name of the Location
    LocationName: Optional[str] = None
    
    # The material package (reel, bin, etc) that is loaded at the position (if any).
    MaterialPackage: Optional[MaterialPackage] = None
    
    # The material carrier that is loaded at the position (if any)
    CarrierInformation: Optional[MaterialCarrier] = None

    def __init__(self, resource_location=None, location_identifier=None, location_name=None, 
                 material_package=None, carrier_information=None):
        self.ResourceLocation = resource_location
        self.LocationIdentifier = location_identifier
        self.LocationName = location_name
        self.MaterialPackage = material_package
        self.CarrierInformation = carrier_information