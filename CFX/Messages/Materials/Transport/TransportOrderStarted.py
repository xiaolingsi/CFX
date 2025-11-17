from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.TransportOrderStatus import TransportOrderStatus
from CFX.Messages.Structures.MaterialPackage import MaterialPackage


@dataclass_json
@dataclass
class TransportOrderStarted(CFXMessage):
    TransportOrderId: str
    StartedBy: Operator
    Comments: str
    Status: TransportOrderStatus
    RelatedWorkOrderId: str
    Source: str
    FinalDestination: str
    NextCheckpoint: str
    Materials: List[MaterialPackage]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transport_order_id: str = "", started_by: Operator = None, comments: str = "", 
                 status: TransportOrderStatus = None, related_work_order_id: str = "", source: str = "", 
                 final_destination: str = "", next_checkpoint: str = "", materials: List[MaterialPackage] = None):
        super().__init__()
        self.type = "CFX.Materials.Transport.TransportOrderStarted,CFX"
        self.message_name = "CFX.Materials.Transport.TransportOrderStarted"
        self.TransportOrderId = transport_order_id
        self.StartedBy = started_by or Operator()
        self.Comments = comments
        self.Status = status or TransportOrderStatus.Unspecified
        self.RelatedWorkOrderId = related_work_order_id
        self.Source = source
        self.FinalDestination = final_destination
        self.NextCheckpoint = next_checkpoint
        self.Materials = materials or []