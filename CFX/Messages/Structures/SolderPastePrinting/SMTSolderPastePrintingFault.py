"""
A specific type of fault that is produced by endpoints responsible
for the printing of solder paste on PCBs.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..Fault import Fault
from .SMTSolderPastePrintingFaultType import SMTSolderPastePrintingFaultType


@dataclass_json
@dataclass
class SMTSolderPastePrintingFault(Fault):
    """
    A specific type of fault that is produced by endpoints responsible
    for the printing of solder paste on PCBs.
    """
    
    # The specific type of printing fault
    PrintingFaultType: SMTSolderPastePrintingFaultType = SMTSolderPastePrintingFaultType.SqueegeeError