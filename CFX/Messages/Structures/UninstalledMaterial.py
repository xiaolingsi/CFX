from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json
from .UninstalledReason import UninstalledReason
from .MaterialPackage import MaterialPackage
from .InstalledComponent import InstalledComponent


@dataclass_json
@dataclass
class UninstalledMaterial:
    """
    Describes when single lot of material that is uninstalled from a production unit, 
    possibly from specific locations on the production unit.
    """
    
    # Unique ID of Production Unit, Panel, or Carrier
    UnitIdentifier: str = ""
    
    # Logical reference of production unit as defined by CFX position rule (see CFX standard section 5.6). 
    UnitPositionNumber: Optional[int] = 0
    
    # The total quantity of parts or material uninstalled of this particular MaterialPackage (lot)
    QuantityUninstalled: float = 0.0
    
    # The reason why the material was uninstalled.
    Reason: UninstalledReason = UninstalledReason.Other
    
    # The material package that was uninstalled (if known)
    Material: Optional[MaterialPackage] = None
    
    # A list of the components that were uninstalled
    UninstalledComponents: List[InstalledComponent] = field(default_factory=list)