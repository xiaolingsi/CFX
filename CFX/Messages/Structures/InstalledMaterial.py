from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, List
from CFX.Messages.Structures.MaterialPackage import MaterialPackage
from CFX.Messages.Structures.MaterialCarrierLocation import MaterialCarrierLocation
from CFX.Messages.Structures.InstalledComponent import InstalledComponent
from CFX.Messages.Structures.NonInstalledComponent import NonInstalledComponent


@dataclass_json
@dataclass
class InstalledMaterial(object):
    """
    Describes a single lot of material that was installed on a production unit, possibly
    in specific locations on the production unit.
    """
    
    UnitIdentifier: Optional[str] = None
    UnitPositionNumber: Optional[int] = 0
    QuantityInstalled: float = 0.0
    QuantityNonInstalled: float = 0.0
    Material: Optional[MaterialPackage] = None
    CarrierLocation: Optional[MaterialCarrierLocation] = None
    InstalledComponents: Optional[List[InstalledComponent]] = None
    NonInstalledComponents: Optional[List[NonInstalledComponent]] = None
    ReferencePartNumber: Optional[str] = None

    def __init__(self):
        self.InstalledComponents = []
        self.NonInstalledComponents = []