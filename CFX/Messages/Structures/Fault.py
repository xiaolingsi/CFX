import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.FaultCause import FaultCause
from CFX.Messages.Structures.FaultSeverity import FaultSeverity
from CFX.Messages.Structures.SideLocation import SideLocation
from CFX.Messages.UnitPojo.Stage import Stage
from CFX.Messages.Structures.AccessType import AccessType


@dataclass_json
@dataclass
class Fault(object):
    AccessType: AccessType
    Cause: FaultCause
    Description: str
    DescriptionTranslations: dict
    DueDateTime: str
    FaultCode: str
    FaultOccurrenceId: uuid.uuid4
    Lane: int
    OccurredAt: str
    Severity: FaultSeverity
    SideLocation: SideLocation
    Stage: Stage
    TransactionID: uuid.uuid4

    def __init__(self, description, fault_code, fault_occurrence_id=uuid.uuid4(), occurred_at=CFXUtils.get_iso8601_time(),
                 severity=FaultSeverity.Information, transaction_id=uuid.uuid4()):
        self.AccessType = AccessType.Unknown
        self.Cause = FaultCause.LoadError
        self.Description = description
        self.DescriptionTranslations = {}
        self.DueDateTime = CFXUtils.get_iso8601_time()
        self.FaultCode = fault_code
        self.FaultOccurrenceId = fault_occurrence_id
        self.Lane = 0
        self.OccurredAt = occurred_at
        self.Severity = severity
        self.SideLocation = SideLocation.Unknown
        self.Stage = Stage()
        self.TransactionID = transaction_id
