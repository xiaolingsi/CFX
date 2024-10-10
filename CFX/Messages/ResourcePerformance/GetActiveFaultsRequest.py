import uuid
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Fault import Fault
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Operator import Operator


@dataclass_json
@dataclass
class GetActiveFaultsRequest(CFXMessage):

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self):
        super().__init__()
        self.type = "CFX.ResourcePerformance.GetActiveFaultsRequest,CFX"
        self.message_name = "CFX.ResourcePerformance.GetActiveFaultsRequest"


if __name__ == '__main__':
    handleFaultRequest = GetActiveFaultsRequest()
    print(handleFaultRequest.to_cfx_json())
