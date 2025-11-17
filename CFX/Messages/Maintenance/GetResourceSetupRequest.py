from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage


@dataclass_json
@dataclass
class GetResourceSetupRequest(CFXMessage):
    CFXHandle: str

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, cfx_handle: str = ""):
        super().__init__()
        self.type = "CFX.Maintenance.GetResourceSetupRequest,CFX"
        self.message_name = "CFX.Maintenance.GetResourceSetupRequest"
        self.CFXHandle = cfx_handle