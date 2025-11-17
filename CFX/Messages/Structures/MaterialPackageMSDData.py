from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from datetime import datetime, timedelta
from .MaterialPackageData import MaterialPackageData
from .MSDLevel import MSDLevel
from .MSDState import MSDState

@dataclass_json
@dataclass
class MaterialPackageMSDData(MaterialPackageData):
    """Describes addition detail for material packages containing moisture 
    sensitive devices"""
    
    # In the case where the MSD material is open and currently exposed to the
    # environment, the date / time when the MSD material will expire rendering it
    # no longer able to be used in production.  Otherwise null.
    ExpirationDateTime: Optional[datetime] = None
    
    # The date / time when this MSD material was originally opened and exposed to
    # the environment
    OriginalExposureDateTime: Optional[datetime] = None
    
    # In the case where the MSD material is open and currently exposed to the environment,
    # the date / time when the material was most recently opened and/or exposed.  Otherwise null.
    LastExposureDateTime: Optional[datetime] = None
    
    # The total amount of time before the MSD expires, rendering it unable to be used in production
    # (assuming the material is open and exposed to the environment)
    RemainingExposureTime: Optional[timedelta] = None
    
    # The level of moisture sensitivity (as defined by IPC/JEDEC J-STD-033C)
    MSDLevel: Optional[MSDLevel] = None
    
    # An enumeration describing the current state of this MSD material
    MSDState: Optional[MSDState] = None