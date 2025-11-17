from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from .TopicSupportType import TopicSupportType


@dataclass_json
@dataclass
class SupportedTopic:
    """
    A data structure that represents a CFX message topic that is supported by a particular CFX endpoint
    """
    
    # The topic name
    TopicName: str = ""
    
    # Indicates the type of support the endpoint has for this topic.
    TopicSupportType: TopicSupportType = TopicSupportType.Publisher
    
    # If an endpoint does not support ALL CFX messages that have been defined for a given CFX topic,
    # then it must explicitly list which messages is does support.  An empty list implies that the 
    # endpoint supports ALL messages of this topic.
    SupportedMessages: List[str] = field(default_factory=list)