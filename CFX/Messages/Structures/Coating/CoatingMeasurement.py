from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.Measurement import Measurement
from CFX.Messages.Structures.Coating.CoatingMeasurementType import CoatingMeasurementType


@dataclass_json
@dataclass
class CoatingMeasurement(Measurement):
    """
    Structure that describes the a particular measurement / reading that was taken by a coating or encapsulation
    endpoint in the course of dispensing.
    """
    
    # The type of reading
    MeasurementType: CoatingMeasurementType = CoatingMeasurementType.FluidPressure
    
    # The value of the reading (expressed in the appropriate units for the ReadingType).
    ActualValue: Optional[float] = None
    
    # The nominal or expected value for this reading (expressed in the appropriate units for the ReadingType).
    ExpectedValue: Optional[float] = None
    
    # The minimum acceptable value for this reading (expressed in the appropriate units for the ReadingType).
    MinAcceptableValue: Optional[float] = None
    
    # The maximum acceptable value for this reading (expressed in the appropriate units for the ReadingType).
    MaxAcceptableValue: Optional[float] = None
    
    # An optional axis position describing the direction in which the coating or encapsulation nozzle displaced.
    # Examples: AxisX, AxisY, AxisZ.
    # NOTE: ADDED in CFX 1.5
    Axis: str = ""
    
    # An optional positive integer for Fluidpressure measurement type of the coating or encapsulation nozzle 
    # in case of second pressure pump is used
    # NOTE: ADDED in CFX 1.5
    FluidPressure: int = 0
    
    # An optional NozzleWidth measurement type of the coating or encapsulation nozzle
    # NOTE: ADDED in CFX 1.5
    NozzleWidth: int = 0
    
    def __init__(self, measurementType=CoatingMeasurementType.FluidPressure, actualValue=None, 
                 expectedValue=None, minAcceptableValue=None, maxAcceptableValue=None, 
                 axis="", fluidPressure=0, nozzleWidth=0):
        super().__init__()
        self.MeasurementType = measurementType
        self.ActualValue = actualValue
        self.ExpectedValue = expectedValue
        self.MinAcceptableValue = minAcceptableValue
        self.MaxAcceptableValue = maxAcceptableValue
        self.Axis = axis
        self.FluidPressure = fluidPressure
        self.NozzleWidth = nozzleWidth
        
        # Set MeasurementName based on MeasurementType if not already set
        if not self.MeasurementName:
            self.MeasurementName = measurementType.value