from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .ResourceInformation import ResourceInformation


@dataclass_json
@dataclass
class VacuumPump(ResourceInformation):
    """
    ** NOTE: ADDED in CFX 1.3 **
    Vacuum pump resource in an Endpoint. It may have a lifecycle independent
    from the Endpoint where it is located (e.g. maintenance operations)
    """
    pass