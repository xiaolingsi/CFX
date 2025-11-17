"""
Describes a particular InstalledComponent for SMT Placement
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from datetime import datetime
from ..InstalledComponent import InstalledComponent
from .SMTHeadAndNozzle import SMTHeadAndNozzle


@dataclass_json
@dataclass
class SMTInstalledComponent(InstalledComponent):
    """
    Describes a particular InstalledComponent for SMT Placement
    """
    
    # The particular Head / Nozzle with which the component has been installed
    HeadAndNozzle: Optional[SMTHeadAndNozzle] = None

    def __init__(self, set_date_time=False):
        super().__init__(set_date_time=set_date_time)