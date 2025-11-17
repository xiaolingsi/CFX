"""
CFX CoreCommunication Messages Package

This package contains all core communication related message classes.
You can import all core communication messages at once using:
    from CFX.Messages.CoreCommunication import *
"""

# Import all core communication message classes
from .AreYouThereRequest import AreYouThereRequest
from .AreYouThereResponse import AreYouThereResponse
from .EndpointConnected import EndpointConnected
from .EndpointShuttingDown import EndpointShuttingDown
from .GetEndpointInformationRequest import GetEndpointInformationRequest
from .GetEndpointInformationResponse import GetEndpointInformationResponse
from .HeartBeat import HeartBeat
from .NotSupportResponse import NotSupportResponse
from .WhoIsThereRequest import WhoIsThereRequest
from .WhoIsThereResponse import WhoIsThereResponse

# Define __all__ for explicit exports
__all__ = [
    'AreYouThereRequest',
    'AreYouThereResponse',
    'EndpointConnected',
    'EndpointShuttingDown',
    'GetEndpointInformationRequest',
    'GetEndpointInformationResponse',
    'HeartBeat',
    'NotSupportResponse',
    'WhoIsThereRequest',
    'WhoIsThereResponse'
]