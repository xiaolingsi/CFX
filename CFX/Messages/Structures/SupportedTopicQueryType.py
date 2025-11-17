from enum import Enum


class SupportedTopicQueryType(Enum):
    """
    Enumeration used for matching an endpoint's capabilities to a list of CFX topics.
    """
    
    # The endpoint must support ALL topics specified in the supported topics list.
    All = "All"
    
    # The endpoint must support one or more of the topics specified in the supported topics list.
    Any = "Any"
    
    # The supported topics list will be ignored.
    Ignore = "Ignore"