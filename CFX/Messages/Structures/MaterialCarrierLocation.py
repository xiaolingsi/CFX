from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from .MaterialCarrier import MaterialCarrier
from .ResourceLocation import ResourceLocation

@dataclass_json
@dataclass
class MaterialCarrierLocation:
    """Describes a specific location on an endpoint where a material carrier may be loaded.
    When applicable, also contains information about the currently loaded carrier, and
    the material package(s) loaded to that carrer."""
    
    # ** NOTE: ADDED in CFX 1.7 **
    # The ResourceLocation on which the material is located (optional)
    # If null, it is assumed that the Resource is the one associated to the source Endpoint
    ResourceLocation: Optional[ResourceLocation] = None
    
    # The unique identifier of the carrier location (barcode or RFID value)
    LocationIdentifier: Optional[str] = None
    
    # The name of the carrier location
    LocationName: Optional[str] = None
    
    # Dynamic structure that defines the carrier that is presently loaded at the carrier location
    CarrierInformation: Optional[MaterialCarrier] = None