from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.TransportOrderStatus import TransportOrderStatus


@dataclass_json
@dataclass
class CheckpointReached(CFXMessage):
    TransportOrderId: str
    Comments: str
    Status: TransportOrderStatus
    TrackedBy: Operator
    RelatedWorkOrderId: str
    Checkpoint: str
    FinalDestination: str
    NextCheckpoint: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transport_order_id: str = "", comments: str = "", status: TransportOrderStatus = None, 
                 tracked_by: Operator = None, related_work_order_id: str = "", checkpoint: str = "", 
                 final_destination: str = "", next_checkpoint: str = ""):
        super().__init__()
        self.type = "CFX.Materials.Transport.CheckpointReached,CFX"
        self.message_name = "CFX.Materials.Transport.CheckpointReached"
        self.TransportOrderId = transport_order_id
        self.Comments = comments
        self.Status = status or TransportOrderStatus.Unspecified
        self.TrackedBy = tracked_by or Operator()
        self.RelatedWorkOrderId = related_work_order_id
        self.Checkpoint = checkpoint
        self.FinalDestination = final_destination
        self.NextCheckpoint = next_checkpoint