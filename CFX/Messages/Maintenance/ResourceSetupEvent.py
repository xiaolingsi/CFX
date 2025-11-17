from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.Resource import Resource


@dataclass_json
@dataclass
class ResourceSetupEvent(CFXMessage):
    EventDateTime: datetime
    ResourceSetup: Resource

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, event_datetime: datetime = None, resource_setup: Resource = None):
        super().__init__()
        self.type = "CFX.Maintenance.ResourceSetupEvent,CFX"
        self.message_name = "CFX.Maintenance.ResourceSetupEvent"
        self.EventDateTime = event_datetime or CFXUtils.get_iso8601_time()
        self.ResourceSetup = resource_setup or Resource()