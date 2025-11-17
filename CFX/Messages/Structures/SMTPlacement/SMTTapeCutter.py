"""
** NOTE: ADDED in CFX 1.3 **
Tape cutter resource in an Endpoint. It may have a lifecycle independent
from the Endpoint where it is located (e.g. maintenance operations)
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..ResourceInformation import ResourceInformation


@dataclass_json
@dataclass
class SMTTapeCutter(ResourceInformation):
    """
    ** NOTE: ADDED in CFX 1.3 **
    Tape cutter resource in an Endpoint. It may have a lifecycle independent
    from the Endpoint where it is located (e.g. maintenance operations)
    """
    pass