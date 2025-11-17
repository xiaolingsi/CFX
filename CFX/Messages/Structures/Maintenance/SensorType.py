from enum import Enum

class SensorType(Enum):
    """** NOTE: ADDED in CFX 1.3 **
    An enumeration indicating the type of sensor that is located in a resource / sub-resource / endpoint
    The type of the sensor (distance, temperature, time etc.). It shall be used together with the SensorUnitOfMeasure"""
    
    # Unknown sensor
    Unkwnown = "Unkwnown"
    # General sensor
    General = "General"
    # Non standard sensor.
    # It shall be used in combination with the CustomSensorType field
    NonStandard = "NonStandard"
    # Temperature sensor
    Temperature = "Temperature"
    # Electric sensor (e.g. voltage)
    Electric = "Electric"
    # Distance sensor
    Distance = "Distance"
    # Time sensor
    Time = "Time"
    # Humidity sensor
    Humidity = "Humidity"
    # Pressure sensor
    Pressure = "Pressure"
    # Torque sensor
    Torque = "Torque"
    # Power sensor
    Power = "Power"
    # Frequency sensor
    Frequency = "Frequency"


class SensorUnitOfMeasure(Enum):
    """The unit of measure of the sensor (meter, degree, hour etc. according to derived SI where applicable).
    It shall be used together with the SensorType"""
    
    # Unknown sensor
    Unkwnown = "Unkwnown"
    # Non standard unit of measure
    # It shall be used in combination with the CustomUnitOfMeasure field
    NonStandard = "NonStandard"
    # Temperature type
    DegreeCelsius = "DegreeCelsius"
    # Voltage
    V = "V"
    # Ampere
    A = "A"
    # Resistance
    Ohm = "Ohm"
    # Distance type
    m = "m"
    # Time type - not SI but accepted by SI
    h = "h"
    # Umidity unit - in SI as grams per cubic meter
    HumidityPercentage = "HumidityPercentage"
    # Pressure type
    Pa = "Pa"
    # Torque unit
    Nm = "Nm"
    # Power unit
    W = "W"
    # Frequency unit
    Hz = "Hz"