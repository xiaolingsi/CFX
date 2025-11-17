"""
Describes a stage (zone) for an endpoint that is an SMT placement machine.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..StageInformation import StageInformation
from ..Stage import Stage


@dataclass_json
@dataclass
class SMTStageInformation(StageInformation):
    """
    Describes a stage (zone) for an endpoint that is an SMT placement machine.
    """
    
    # The number of stations where a feeder may be mounted for this stage.
    NumberOfFeederStations: int = 0

    def __init__(self, stage: Stage = None, number_of_feeder_stations: int = 0):
        super().__init__(stage=stage)
        self.NumberOfFeederStations = number_of_feeder_stations