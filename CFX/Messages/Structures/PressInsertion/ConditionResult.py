"""
Copyright 2018 TE Connectivity

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-------------------------------------------------------------------------
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
import uuid
from ..UnitPosition import UnitPosition
from ..Operator import Operator
from ..StatusResult import StatusResult
from .Condition import Condition


@dataclass_json
@dataclass
class ConditionResult:
    """
    Describes result of a condition step.
    """
    
    # The barcode, RFID, etc. that was most recently acquired by the scanner / reader.  If a single production unit is moving through the
    # process, this would be the actual unique identifier of that individual unition unit.  However, if multiple production units are moving
    # through the process as a group (as in the case of a PCB panel, a fixture, or any sort of carrier), this would be an identifier that
    # represents the entire group of units, such as a carrier UID, a PCB panel UID, etc.
    PrimaryIdentifier: str = ""
    
    # The Hermes BoardId of the carrier, a PCB panel or single production unit. If a single production unit is moving through the
    # process, this would be the actual unique identifier of that individual unition unit.  However, if multiple production units are moving
    # through the process as a group (as in the case of a PCB panel, a fixture, or any sort of carrier), this would be an identifier that
    # represents the entire group of units, such as a carrier UID, a PCB panel UID, etc.
    # HermesIdentifier will be transfered between all machines which support Hermes. The PrimaryIdentifier is containing a barcode information.
    # Both can be transferred.
    # Remarks:
    # Espcially when the line does not support the Hermes standard in the hole line, the Hermes Identifier can be unique only in the a part
    # of the line. The Primary Identifier can be used to correlate the parts of hermes sublines to correlate this data as well.
    HermesIdentifier: str = ""
    
    # Transaction ID used to attach events and data during subsequent processing, until WorkCompleted
    TransactionID: str = field(default_factory=lambda: str(uuid.uuid4()))
    
    # Data that identifies each specific instance of production unit with a carrier or panel.
    Units: List[UnitPosition] = field(default_factory=list)
    
    # Describes Condition sequence that was executed
    ConditionSequence: Condition = field(default_factory=Condition)
    
    # Describes result of the condition sequence
    ConditionStatus: StatusResult = StatusResult.Success
    
    # Describes the Operator who ran the condition step (optional)
    ConditionOperator: Operator = field(default_factory=Operator)