from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from dataclasses_json import dataclass_json

if TYPE_CHECKING:
    from typing import Self


@dataclass_json
@dataclass
class MaterialPackage:
    """Describes a specific, single handling unit of a particular material, such as a reel of SMT parts,
    a bag of parts, bin of parts, etc."""
    
    # The Unique identifier of the material package (barcode/RFID that identifies
    # this specific material package.
    UniqueIdentifier: Optional[str] = None
    
    # The internal part number of the material package
    InternalPartNumber: Optional[str] = None
    
    # ** NOTE: ADDED in CFX 1.5 **
    # The internal package name of the material package
    InternalPackageName: Optional[str] = None
    
    # The quantity of parts or material contained within this material package.
    Quantity: float = 0.0
    
    # Gets or sets the next spliced material package.
    # When placement machine is using tape material, operator can splice a new tape onto an existing material.
    # This will lead to a chain of material. Physically, the existing reel with barcode will be separated from the
    # already mounted tape and a new tape with its reel will be appended to the material. This leads to a situation that
    # the material chain can only be identified by the newest material added to the chain (known as the "trailing" material package)
    # using the barcode on its reel. Typically, the placement machine is consuming from the "leading" material package of the chain.
    # So the assumption is that we may build a chain B->A by splicing B to A, where A is the "leading"
    # material package (consumed first), and B is the "trailing" material package (consumed last). In this situation, the chain
    # will be identified only by the barcode of B, and the MaterialPackage structure of B will have its LeadingMaterialPackage
    # property set to A. It should be noted that it is possible and permissible to form chains of more than 2 material packages.
    # In this situation, each material package in the chain will have the LeadingMaterialPackage property set to the next package
    # in the chain (with the exception of the material package that is currently being consumed (the "leading" material package).
    # The next material package in the chain (heading towards the consumption point).
    LeadingMaterialPackage: Optional['Self'] = None
    
    # Gets or sets the batch identifier.
    # There is material in the factory where not each material unit is identifiable. This is the case for
    # Trays for example. Trays are delivered as a batch of trays. But each tray does not have a unique ID, only
    # the batch of trays has a unique ID.
    # In this case, we assume that the unique Batch ID is in the property
    # BatchID and each tray which has been mounted will get a temporary UniqueIdentifier as long as it has been
    # mounted on the machine. See BatchMaterialPackage for more details.
    BatchId: Optional[str] = None
    
    # Gets or sets the batch material package.
    # This field specifies the parent batch material unit representing the complete batch.
    # The BatchMaterialPackage can be queried for quantity as well as other properties for the whole batch.
    # This data is only set when events are sent out of the line level verification system. This
    # property cannot be set via the interface. 
    BatchMaterialPackage: Optional['Self'] = None
    
    # Gets or sets the grey zone.
    # This specifies the grey zone between 2 material packages. A grey zone is a zone
    # where the placement system cannot determine where the switch between 2 material packages
    # has taken place. Therefore the system tracks both material packages.
    # The quality of the GreyZone is driven by the process the customer is operating and if
    # the feeder are using optional splice sensor detectors or not.
    # Background is, that some sensors can detect a splice plate and a splice plate has a length
    # which covers a number of components which hide the real end of the tape. Therefore the verification system
    # will report a greyzone between the "leading package" and the "trailing" in the chain.
    # The greyzone will be maintained typically by the machine, based on the feeder configuration. When the feeder has a splice sensor,
    # the grey zone will be calculated when the sensor detects a splice, and will be adjusted when components are consumed.
    # When the greyzone reaches zero, the "leading" package will be consumed and the chain will be modified by removing the "leading" package
    # from the chain, resulting in the next package in the chain becoming the new "leading" package.
    GreyZone: float = 0.0

    def __init__(self, unique_identifier=None, internal_part_number=None, internal_package_name=None, 
                 quantity=0.0, leading_material_package=None, batch_id=None, 
                 batch_material_package=None, grey_zone=0.0):
        self.UniqueIdentifier = unique_identifier
        self.InternalPartNumber = internal_part_number
        self.InternalPackageName = internal_package_name
        self.Quantity = quantity
        self.LeadingMaterialPackage = leading_material_package
        self.BatchId = batch_id
        self.BatchMaterialPackage = batch_material_package
        self.GreyZone = grey_zone