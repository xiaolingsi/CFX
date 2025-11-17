"""
CFX Maintenance Messages Package

This package contains all maintenance related message classes.
You can import all maintenance messages at once using:
    from CFX.Messages.Maintenance import *
"""

# Import all maintenance message classes
from .GetResourceInformationRequest import GetResourceInformationRequest
from .GetResourceInformationResponse import GetResourceInformationResponse
from .GetResourceMaintenanceAndServiceRequest import GetResourceMaintenanceAndServiceRequest
from .GetResourceMaintenanceAndServiceResponse import GetResourceMaintenanceAndServiceResponse
from .GetResourceMaintenanceStatusRequest import GetResourceMaintenanceStatusRequest
from .GetResourceMaintenanceStatusResponse import GetResourceMaintenanceStatusResponse
from .GetResourceSetupRequest import GetResourceSetupRequest
from .GetResourceSetupResponse import GetResourceSetupResponse
from .ResourceInformationEvent import ResourceInformationEvent
from .ResourceMaintenanceAndServiceEvent import ResourceMaintenanceAndServiceEvent
from .ResourceMaintenanceStatusEvent import ResourceMaintenanceStatusEvent
from .ResourceSetupEvent import ResourceSetupEvent

# Define __all__ for explicit exports
__all__ = [
    'GetResourceInformationRequest',
    'GetResourceInformationResponse',
    'GetResourceMaintenanceAndServiceRequest',
    'GetResourceMaintenanceAndServiceResponse',
    'GetResourceMaintenanceStatusRequest',
    'GetResourceMaintenanceStatusResponse',
    'GetResourceSetupRequest',
    'GetResourceSetupResponse',
    'ResourceInformationEvent',
    'ResourceMaintenanceAndServiceEvent',
    'ResourceMaintenanceStatusEvent',
    'ResourceSetupEvent'
]