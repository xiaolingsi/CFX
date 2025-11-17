from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ResourceInformation import ResourceInformation


@dataclass_json
@dataclass
class Gantry(ResourceInformation):
    """
    Gantry resource in an Endpoint. It may have a lifecycle independent
    from the Endpoint where it is located (e.g. maintenance operations)
    """
    
    pass