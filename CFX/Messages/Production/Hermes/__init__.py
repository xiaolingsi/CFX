"""
CFX Production Hermes Messages Package

This package contains all Hermes related message classes.
You can import all Hermes messages at once using:
    from CFX.Messages.Production.Hermes import *
"""

# Import all Hermes message classes
from .GetMagazineDataRequest import GetMagazineDataRequest
from .GetMagazineDataResponse import GetMagazineDataResponse
from .GetWorkOrderDataRequest import GetWorkOrderDataRequest
from .GetWorkOrderDataResponse import GetWorkOrderDataResponse
from .MagazineArrived import MagazineArrived
from .MagazineDeparted import MagazineDeparted

# Define __all__ for explicit exports
__all__ = [
    'GetMagazineDataRequest',
    'GetMagazineDataResponse',
    'GetWorkOrderDataRequest',
    'GetWorkOrderDataResponse',
    'MagazineArrived',
    'MagazineDeparted'
]