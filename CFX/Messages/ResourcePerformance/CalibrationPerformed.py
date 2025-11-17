from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Calibration import Calibration


@dataclass_json
@dataclass
class CalibrationPerformed(CFXMessage):
    """
    Sent when calibration of any sort has been performed at an endpoint.
    """
    Calibration: Calibration = field(default_factory=Calibration)

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, calibration=None):
        super().__init__()
        self.type = "CFX.ResourcePerformance.CalibrationPerformed,CFX"
        self.message_name = "CFX.ResourcePerformance.CalibrationPerformed"
        self.Calibration = calibration if calibration is not None else Calibration()
