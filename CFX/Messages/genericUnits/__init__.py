"""
CFX genericUnits Package

This package contains all generic unit classes.
You can import all generic units at once using:
    from CFX.Messages.genericUnits import *
"""

# Import all generic unit classes
from .RequestResult import RequestResult
from .StageType import StageType
from .StatusResult import StatusResult
from .SupportedTopic import SupportedTopic
from .SupportedTopicQueryType import SupportedTopicQueryType
from .TopicSupportType import TopicSupportType
from .WorkResult import WorkResult
from .WorkStagePauseReason import WorkStagePauseReason

# Define __all__ for explicit exports
__all__ = [
    'RequestResult',
    'StageType',
    'StatusResult',
    'SupportedTopic',
    'SupportedTopicQueryType',
    'TopicSupportType',
    'WorkResult',
    'WorkStagePauseReason'
]