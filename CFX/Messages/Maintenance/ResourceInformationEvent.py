from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Resource import Resource


@dataclass_json
@dataclass
class ResourceInformationEvent(CFXMessage):
    EventDateTime: datetime
    ResourceInformation: Resource

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, event_datetime: datetime = None, resource_information: Resource = None):
        super().__init__()
        self.type = "CFX.Maintenance.ResourceInformationEvent,CFX"
        self.message_name = "CFX.Maintenance.ResourceInformationEvent"
        self.EventDateTime = event_datetime
        self.ResourceInformation = resource_information or Resource()