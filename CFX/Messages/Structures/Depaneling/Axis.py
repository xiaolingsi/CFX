from dataclasses import dataclass
from dataclasses_json import dataclass_json
from decimal import Decimal


@dataclass_json
@dataclass
class Axis(object):
    """
    Represents an axis on a depaneling / router type machine.
    NOTE: ADDED in CFX 1.5
    """
    
    # Name of the Axis 
    AxisName: str = ""
    
    # Max axis speed in mm/s
    ActualAxisSpeed: Decimal = Decimal("0.0")
    
    # Set value in (mm/s2)
    AxisAcceleration_SetValue: Decimal = Decimal("0.0")
    
    # Set value in (mm/s2)
    AxisDecceleration_SetValue: Decimal = Decimal("0.0")
    
    # Operating at Maximum speed.
    ActualMaxVelocity: Decimal = Decimal("0.0")
    
    def __init__(self, axisName="", actualAxisSpeed=Decimal("0.0"), 
                 axisAcceleration_SetValue=Decimal("0.0"), 
                 axisDecceleration_SetValue=Decimal("0.0"), 
                 actualMaxVelocity=Decimal("0.0")):
        self.AxisName = axisName
        self.ActualAxisSpeed = actualAxisSpeed
        self.AxisAcceleration_SetValue = axisAcceleration_SetValue
        self.AxisDecceleration_SetValue = axisDecceleration_SetValue
        self.ActualMaxVelocity = actualMaxVelocity