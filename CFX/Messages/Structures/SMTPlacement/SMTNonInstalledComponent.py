"""
Describes a particular NonInstalledComponent for SMT Placement
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from datetime import datetime
from ..NonInstalledComponent import NonInstalledComponent
from .SMTHeadAndNozzle import SMTHeadAndNozzle


@dataclass_json
@dataclass
class SMTNonInstalledComponent(NonInstalledComponent):
    """
    Describes a particular NonInstalledComponent for SMT Placement
    """
    
    # The particular Head / Nozzle with which the component has not been installed
    HeadAndNozzle: Optional[SMTHeadAndNozzle] = None

    def __init__(self, set_date_time=False):
        super().__init__(setDateTime=set_date_time)