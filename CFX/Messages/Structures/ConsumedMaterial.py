from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.Messages.Structures.MaterialLocation import MaterialLocation


@dataclass_json
@dataclass
class ConsumedMaterial:
    """
    Describes an event where material is consumed in course of production.
    """
    MaterialLocation: Optional[MaterialLocation] = None
    QuantityUsed: float = 0.0
    QuantitySpoiled: float = 0.0
    RemainingQuantity: float = 0.0

    def __init__(self, material_location=None, quantity_used=0.0, quantity_spoiled=0.0, remaining_quantity=0.0):
        self.MaterialLocation = material_location
        self.QuantityUsed = quantity_used
        self.QuantitySpoiled = quantity_spoiled
        self.RemainingQuantity = remaining_quantity