from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from ..Recipe import Recipe
from .Panel import Panel

@dataclass_json
@dataclass
class PCBInspectionRecipe(Recipe):
    """Represents a specialized type of recipe that is used to drive the inspection of
    a Printed Circuit Board (PCB) by a piece of inspection equipment (such as an AOI or SPI machine),
    or by a human inspector."""
    
    # A data structure representing the PCB panel that is to be inspected.  
    # This could be a single PCB, an panel with multiple PCBs, or even a structure
    # of PCBs containing sub-PCBs.
    Panel: Optional[Panel] = None