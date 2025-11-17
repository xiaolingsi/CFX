from CFX.CFXMessage import CFXMessage
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.Messages.genericUnits.SupportedTopicQueryType import SupportedTopicQueryType
from CFX.Messages.genericUnits.SupportedTopic import SupportedTopic


@dataclass_json
@dataclass
class WhoIsThereRequest(CFXMessage):
    SupportedTopicQueryType: SupportedTopicQueryType
    SupportedTopics: list

    def __init__(self,supportedTopicQueryType:SupportedTopicQueryType = SupportedTopicQueryType.All):
        super().__init__()
        self.type = "CFX.WhoIsThereRequest,CFX"
        self.message_name = "CFX.WhoIsThereRequest"
        self.SupportedTopicQueryType = supportedTopicQueryType
        self.SupportedTopics = list()

    def add_supported_topic(self,supportTopic:SupportedTopic):
        self.SupportedTopics.append(supportTopic)

    def to_cfx_json(self):
        return self.to_json()

