from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from datetime import datetime

from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.CalibrationType import CalibrationType
from CFX.Messages.Structures.OperationStatus import OperationStatus


@dataclass_json
@dataclass
class Calibration(object):
    CalibrationCode: Optional[str] = None
    CalibrationType: Optional[CalibrationType] = CalibrationType.Unkwnown
    Comments: Optional[str] = None
    Status: Optional[OperationStatus] = None
    CalibrationTime: Optional[datetime] = None
    """
    A dynamic structure describing a calibration event.
    """
    def __init__(self):
        self.CalibrationCode: Optional[str] = "123"
        self.CalibrationType: Optional[CalibrationType] = CalibrationType.Unkwnown
        self.Comments: Optional[str] = None
        self.Status: Optional[OperationStatus] = OperationStatus.Unknown
        self.CalibrationTime: Optional[datetime] = None or CFXUtils.get_iso8601_time()
