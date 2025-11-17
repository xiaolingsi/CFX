from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class MaterialPackageData:
    """An abstract base class from which dynamic material data structures derive.
    For example, MaterialPackageMSDData"""
    
    pass