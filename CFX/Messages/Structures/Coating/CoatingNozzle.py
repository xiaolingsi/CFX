from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.Coating.CoatingNozzleType import CoatingNozzleType


@dataclass_json
@dataclass
class CoatingNozzle(Stage):
    """
    A specialized type of Stage that represents a Nozzle within a Coating Machine.
    NOTE: ADDED in CFX 1.5
    """
    
    # The type/purpose of this Nozzle.
    CoatingNozzleType: CoatingNozzleType = CoatingNozzleType.Jetter
    
    def __init__(self, coatingNozzleType=CoatingNozzleType.Jetter, stageSequence=0, 
                 stageName="", stageType=None):
        super().__init__(stageSequence, stageName, stageType)
        self.CoatingNozzleType = coatingNozzleType