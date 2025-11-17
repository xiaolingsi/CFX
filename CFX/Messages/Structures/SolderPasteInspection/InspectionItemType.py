"""
** NOTE: ADDED in CFX 1.3 **
Provide information of the inspection object type
"""

from enum import Enum
from dataclasses_json import dataclass_json


class InspectionItemType(Enum):
    """
    ** NOTE: ADDED in CFX 1.3 **
    Provide information of the inspection object type
    """
    
    # Unknown object
    Unknown = 0
    
    # General object not specifically modelled in this enumeration
    General = 1
    
    # Printed Circuit Board with 1:n Unit(s)
    PCB = 2
    
    # CFX Unit 
    Unit = 3
    
    # Fiducial of the unit inspected
    Fiducial = 4
    
    # Barcode, 1D, 2D
    Barcode = 5
    
    # Component on a unit
    Component = 6
    
    # Pin of a given component
    Pin = 7
    
    # 2D PCB location
    Pad = 8
    
    # Solder deposit
    SolderDeposit = 9