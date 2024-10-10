from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class WorkOrderIdentifier(object):
    WorkOrderId: str
    Batch: str

    def __init__(self, work_order_id, batch):
        self.WorkOrderId = work_order_id
        self.Batch = batch
