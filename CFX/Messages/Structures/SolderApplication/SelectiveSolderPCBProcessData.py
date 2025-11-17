"""
Process Data specific to a single PCB within a group of PCB's that are selectively
soldered.
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from ..ProcessData import ProcessData
from .ZoneData import ZoneData


@dataclass_json
@dataclass
class SelectiveSolderPCBProcessData(ProcessData):
    """
    Process Data specific to a single PCB within a group of PCB's that are selectively
    soldered.
    """
    
    # Data sepcific to a single zone with the
    # Selective Soldering System
    ZoneData: List[ZoneData] = field(default_factory=list)