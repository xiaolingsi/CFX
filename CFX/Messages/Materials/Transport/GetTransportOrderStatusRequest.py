from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class GetTransportOrderStatusRequest(CFXMessage):
    TransportOrderId: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, transport_order_id: str = ""):
        super().__init__()
        self.type = "CFX.Materials.Transport.GetTransportOrderStatusRequest,CFX"
        self.message_name = "CFX.Materials.Transport.GetTransportOrderStatusRequest"
        self.TransportOrderId = transport_order_id