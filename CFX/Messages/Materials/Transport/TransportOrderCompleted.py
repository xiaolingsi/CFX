from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class TransportOrderCompleted(CFXMessage):
    TransportOrderId: str
    Comments: str
    AcceptedBy: Operator
    RelatedWorkOrderId: str
    FinalDestination: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transport_order_id: str = "", comments: str = "", accepted_by: Operator = None, 
                 related_work_order_id: str = "", final_destination: str = ""):
        super().__init__()
        self.type = "CFX.Materials.Transport.TransportOrderCompleted,CFX"
        self.message_name = "CFX.Materials.Transport.TransportOrderCompleted"
        self.TransportOrderId = transport_order_id
        self.Comments = comments
        self.AcceptedBy = accepted_by or Operator()
        self.RelatedWorkOrderId = related_work_order_id
        self.FinalDestination = final_destination