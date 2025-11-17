from CFX.Messages.genericUnits.TopicSupportType import TopicSupportType
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class SupportedTopic(object):
    TopicName: str
    TopicSupportType: TopicSupportType
    SupportedMessages: list

    def __init__(self,topicName="",topicSupportType = TopicSupportType.Publisher):
        self.TopicName = topicName
        self.TopicSupportType = topicSupportType
        self.SupportedMessages = list()

    def add_support_message(self,support_message:str):
        self.SupportedMessages.append(support_message)


