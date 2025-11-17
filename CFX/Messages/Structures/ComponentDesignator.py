from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from CFX.Messages.Structures.UnitPosition import UnitPosition


@dataclass_json
@dataclass
class ComponentDesignator(object):
    """
    Represents and identifies a particular component (instance of a part) on a production unit, or a particular aspect
    of a particular component, such as an individual pin of an electronic component.
    """
    
    ReferenceDesignator: Optional[str] = None
    UnitPosition: Optional[UnitPosition] = None
    PartNumber: Optional[str] = None

    def __init__(self):
        self.UnitPosition = None