from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class MaintenanceTask:
    """
    Represents a task that was performed during a maintenance operation.
    """
    Task: Optional[str] = None
    TaskId: Optional[str] = None
    Operator: Optional[Operator] = None
    ManHoursConsumed: float = 0.0

    def __init__(self, task=None, task_id=None, operator=None, man_hours_consumed=0.0):
        self.Task = task
        self.TaskId = task_id
        self.Operator = operator
        self.ManHoursConsumed = man_hours_consumed
