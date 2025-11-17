from enum import Enum


class CoatingMeasurementType(Enum):
    """
    An enumeration indicating the type of measurement made within a coating or encapsulation machine.
    """
    
    # The pressure of the coating or encapsulation nozzle, expressed in kilo Pascals (kPa)
    FluidPressure = "FluidPressure"
    
    # The total volume of fluid dispensed, expressed in cubic centimeters (cc)
    FluidVolume = "FluidVolume"
    
    # The Heating value of the coating or encapsulation nozzle, expressed in grad
    # NOTE: ADDED in CFX 1.5
    Heater = "Heater"
    
    # The Heating value of the coating or encapsulation nozzle measured through sensor, expressed in grad
    # NOTE: ADDED in CFX 1.5
    Monitor = "Monitor"
    
    # The axis position describing the direction in which the coating or encapsulation nozzle displaced, expressed in millimeter(mm)
    # NOTE: ADDED in CFX 1.5
    Axis = "Axis"
    
    # The total volume of fluid tested after n number of units processed, expressed in grams (g)
    # NOTE: ADDED in CFX 1.5
    Fluidweight = "Fluidweight"
    
    # The level of fluid tested from the container or Beaker, expressed in millimeter(mm)
    # NOTE: ADDED in CFX 1.5
    MaterialLevel = "MaterialLevel"
    
    # The Width of adjustable Nozzle Eg. Curtain Nozzle, expressed in millimeter(mm)
    # NOTE: ADDED in CFX 1.5
    NozzleWidth = "NozzleWidth"