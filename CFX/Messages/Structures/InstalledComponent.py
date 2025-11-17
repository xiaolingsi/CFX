from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from datetime import datetime

from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.ComponentElectricalTest import ComponentElectricalTest


@dataclass_json
@dataclass
class InstalledComponent(object):
    """
    Describes a particular location on a production unit where materials / parts were installed.
    """
    
    ReferenceDesignator: Optional[str] = None
    InstallationTime: Optional[datetime] = None
    Stage: Optional[Stage] = None
    ElectricalTest: Optional[ComponentElectricalTest] = None

    def __init__(self, set_date_time=False):
        if set_date_time:
            self.InstallationTime = CFXUtils.get_iso8601_time()