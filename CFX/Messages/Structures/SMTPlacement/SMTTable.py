"""
** NOTE: ADDED in CFX 1.3 **
Table (also know as change over table) resource in an Endpoint's setup.
It may have a lifecycle independent from the Endpoint where it is located (e.g. maintenance operations)
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..ResourceInformation import ResourceInformation


@dataclass_json
@dataclass
class SMTTable(ResourceInformation):
    """
    ** NOTE: ADDED in CFX 1.3 **
    Table (also know as change over table) resource in an Endpoint's setup.
    It may have a lifecycle independent from the Endpoint where it is located (e.g. maintenance operations)
    """
    pass