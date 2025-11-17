"""
CFX Production TestAndInspection Messages Package

This package contains all test and inspection related message classes.
You can import all test and inspection messages at once using:
    from CFX.Messages.Production.TestAndInspection import *
"""

# Import all test and inspection message classes
from .GetInspectionInfoRequest import GetInspectionInfoRequest
from .GetInspectionInfoResponse import GetInspectionInfoResponse
from .UnitsInspected import UnitsInspected
from .UnitsTested import UnitsTested

# Define __all__ for explicit exports
__all__ = [
    'GetInspectionInfoRequest',
    'GetInspectionInfoResponse',
    'UnitsInspected',
    'UnitsTested'
]