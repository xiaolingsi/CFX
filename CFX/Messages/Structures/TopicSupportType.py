from enum import Enum


class TopicSupportType(Enum):
    """
    Indicates the type of support an endpoint has for a particular topic.
    """
    
    # The endpoint publishes outbound messages for this topic, and responds to inbound requests
    Publisher = "Publisher"
    
    # The endpoint consumes the messages of this topic that are produced by other endpoints
    Consumer = "Consumer"
    
    # The endpoint publishes outbound messages for this topic, responds to inbound request, and
    # consumes the messages of this topic that are produced by other endpoints
    PublisherConsumer = "PublisherConsumer"