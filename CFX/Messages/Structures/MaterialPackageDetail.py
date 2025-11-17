from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import datetime
from .MaterialPackage import MaterialPackage
from .MaterialStatus import MaterialStatus
from .HazardousMaterialType import HazardousMaterialType
from .MaterialPackageData import MaterialPackageData
from .PackagingInfo import PackagingInfo
from .ResourceLocation import ResourceLocation
from ...CFXUtils import CFXUtils


@dataclass_json
@dataclass
class MaterialPackageDetail:
    """Describes detailed information about a particular material package (instance of
    material that is tracked, stocked, and used within the factory environment."""
    
    def __init__(self):
        self.Created = CFXUtils.get_iso8601_time()
    
    # The unique identifier of the material package
    UniqueIdentifier: Optional[str] = None
    
    # The internal part number of the material contained within this material package
    InternalPartNumber: Optional[str] = None
    
    # ** NOTE: ADDED in CFX 1.5 **
    # The internal package name of the material package
    InternalPackageName: Optional[str] = None
    
    # The name of the manufacturer of this material
    Manufacturer: Optional[str] = None
    
    # The part number of the material as it is known to the original manufacturer of the material
    ManufacturerPartNumber: Optional[str] = None
    
    # The name of the supplier from whom the material was purchased / supplied.
    Vendor: Optional[str] = None
    
    # The part number of the material as it is known to the supplier or vendor of the material
    VendorPartNumber: Optional[str] = None
    
    # The lot code applied to this batch of material by the original manufacturer of the material
    ManufacturerLotCode: Optional[str] = None
    
    # The date / time when this material package was introduced into the factory environment
    Created: Optional[datetime] = CFXUtils.get_iso8601_time()
    
    # The date / time when this material was originally manufactured by the manufacturer
    ManufactureDate: Optional[datetime] = CFXUtils.get_iso8601_time()
    
    # The date / time when this material was received into the factory
    ReceivedDate: Optional[datetime] = CFXUtils.get_iso8601_time()
    
    # Gets or sets the expiry date of this material package based on manufacture definitions.
    ExpiryDate: Optional[datetime] = CFXUtils.get_iso8601_time()
    
    # The unit of measure for this material (items, liters, meters, grams, etc.)
    # Only valid SI units of measure should be utilized
    Units: Optional[str] = None
    
    # The initial quantity of material contained within this material package at the time
    # when it was initialized / introduced into the factory environment
    InitialQuantity: float = 0.0
    
    # The quantity of material presently contained within this material package
    Quantity: float = 0.0
    
    # The current status of this material package
    Status: Optional[MaterialStatus] = MaterialStatus.Depleted
    
    # Specifies whether or not a material is hazardous, and if so, the regulatory directive that controls
    # the use of this substance in production.
    HazardousMaterialType: Optional[HazardousMaterialType] = HazardousMaterialType.Hazardous
    
    # Optional dynamic structure containing specialized information about this material package.
    # For example, if the material package contains moisture sensitive devices, this would contain
    # additional information specific to MSD material handling (exposure time, etc.).
    MaterialData: Optional[MaterialPackageData] = None
    
    # ** NOTE: ADDED in CFX 1.5 **
    # Gets or sets the batch identifier.
    # There is material in the factory where not each material unit is identifiable. This is the case for
    # Trays for example. Trays are delivered as a batch of trays. But each tray does not have a unique ID, only
    # the batch of trays has a unique ID.
    # In this case, we assume that the unique Batch ID is in the property
    # BatchID and each tray which is been mounted will get a temporary UniqueIdentifier as long as it is been
    # mounted on the machine. See BatchMaterialPackage for more details.
    BatchId: Optional[str] = None
    
    # ** NOTE: ADDED in CFX 1.5 **
    # Gets or sets the grey zone.
    # This specifies the grey zone between 2 material packages. A grey zone is a zone
    # where the placement system can not determine where the switch between 2 material packages
    # has been taken place. Therefore the system tracks both material packages.
    # The quality of the GreyZone is driven by the process the customer is operating and if
    # the feeder are using optional splice sensor detectors or not.
    # Background is, that some sensors can detect the splice plate and the splice plate has a length
    # which covers a number of components which hide the real end of tape. Therefore the verifcation system
    # will report a greyzone between the "leading package" and the "trailing" in the chain.
    # The greyzone will be maintained typically by the machine, based on the feeder configuration. When the feeder has a sploice sensor the
    # grey zone will be calculated when the sensor detects the splice, and will be adjusted when components are consumed.
    # When the greyzone reached zero, the "leading" package will be consumed and the chain will be modified by removing the "leading" package
    # from the chain, resulting in the next package in the chain becoming the new "leading" package.
    GreyZone: float = 0.0
    
    # ** NOTE: ADDED in CFX 1.5 **
    # The price of a part in the material package
    PartPrice: float = 0.0
    
    # ** NOTE: ADDED in CFX 1.5 **
    # The unit of the price of a part in the material package
    PartPriceUnit: Optional[str] = None
    
    # ** NOTE: ADDED in CFX 1.5 **
    # The unit of the price of a part in the material package
    PackagingInfo: Optional[PackagingInfo] = None
    
    # ** NOTE: ADDED in CFX 1.7 **
    # The ResourceLocation on which the material is located (optional)
    # If null, it is assumed that the Resource is the one associated to the source Endpoint
    ResourceLocation: Optional[ResourceLocation] = None