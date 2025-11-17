from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ProcessData import ProcessData
from CFX.Messages.Structures.Cleaning.CleaningStep import CleaningStep


@dataclass_json
@dataclass
class CleaningProcessData(ProcessData):
    """
    Data for the cleaning process, applied to production units – this is the defluxing process – and tools, e.g. squeegees, stencils, etc.
    The defluxing process removes flux-deposits after reflow and takes care of cleaning 
    a production unit or a batch of production units. Cleaning of tools removes deposits, 
    e.g.solder paste, from tools, so that they can continued to be used.
    NOTE: ADDED in CFX 1.5
    """
    
    # The speed (in cm / minute) of the conveyor
    ConveyorSpeed: float = 0.0
    
    # Cleaning time as specified in recipe expressed in seconds (s)
    CleaningTimeSet: float = 0.0
    
    # Actual cleaning time expressed in seconds (s)
    CleaningTimeActual: float = 0.0
    
    # A list of cleaning steps
    CleaningSteps: List[CleaningStep] = field(default_factory=list)
    
    def __init__(self, conveyorSpeed=0.0, cleaningTimeSet=0.0, cleaningTimeActual=0.0, cleaningSteps=None):
        super().__init__()
        self.ConveyorSpeed = conveyorSpeed
        self.CleaningTimeSet = cleaningTimeSet
        self.CleaningTimeActual = cleaningTimeActual
        self.CleaningSteps = cleaningSteps if cleaningSteps is not None else []