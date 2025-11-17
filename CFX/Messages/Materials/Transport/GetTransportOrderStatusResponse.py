from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.TransportOrderStatus import TransportOrderStatus
from CFX.Messages.Structures.TransportOrderHistory import TransportOrderHistory


@dataclass_json
@dataclass
class GetTransportOrderStatusResponse(CFXMessage):
    Result: RequestResult
    TransportOrderId: str
    FinalDestination: str
    Status: TransportOrderStatus
    History: List[TransportOrderHistory]

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, transport_order_id: str = "", 
                 final_destination: str = "", status: TransportOrderStatus = None, 
                 history: List[TransportOrderHistory] = None):
        super().__init__()
        self.type = "CFX.Materials.Transport.GetTransportOrderStatusResponse,CFX"
        self.message_name = "CFX.Materials.Transport.GetTransportOrderStatusResponse"
        self.Result = result or RequestResult()
        self.TransportOrderId = transport_order_id
        self.FinalDestination = final_destination
        self.Status = status or TransportOrderStatus.Unspecified
        self.History = history or []