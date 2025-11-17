from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .. import Fault, ComponentDesignator, MaterialLocation
from .THTInsertionFaultType import THTInsertionFaultType

@dataclass_json
@dataclass
class THTInsertionFault(Fault):
    """
    A specific type of fault that is produced by endpoints responsible
    for the insertion of through-hole electronic components (THT insertion)
    """
    def __init__(self):
        super().__init__()
        self.insertion_fault_type: THTInsertionFaultType = THTInsertionFaultType.InsertionError
        self.designator: ComponentDesignator = ComponentDesignator()
        self.material_location: MaterialLocation = MaterialLocation()

    insertion_fault_type: THTInsertionFaultType
    program_step: int
    designator: ComponentDesignator
    material_location: MaterialLocation