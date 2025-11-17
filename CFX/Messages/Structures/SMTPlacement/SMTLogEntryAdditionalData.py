"""
** NOTE: ADDED in CFX 1.4 **
A specialized type of LogEntryRecordedData for an SMT machine
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from ..LogEntryAdditionalData import LogEntryAdditionalData
from .SMTHeadAndNozzle import SMTHeadAndNozzle


@dataclass_json
@dataclass
class SMTLogEntryAdditionalData(LogEntryAdditionalData):
    """
    ** NOTE: ADDED in CFX 1.4 **
    A specialized type of LogEntryRecordedData for an SMT machine
    """
    
    # The particular Head/Nozzle related to the log entry (where applicable)
    HeadAndNozzle: Optional[SMTHeadAndNozzle] = None