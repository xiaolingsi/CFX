from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class EnergyConsumptionRequest(CFXMessage):
    """
    This request allows an external source to inquire data regarding energy consumption of the endpoint.
    ** NOTE: ADDED in CFX 1.3 **
    """

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self):
        super().__init__()
        self.type = "CFX.ResourcePerformance.EnergyConsumptionRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.EnergyConsumptionRequest"