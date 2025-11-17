import enum


class TopicSupportType(enum.Enum):
    Publisher = 0
    Consumer = 1
    PublisherConsumer = 2
