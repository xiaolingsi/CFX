from enum import Enum


class CleaningReadingType(Enum):
    """
    An enumeration indicating the type of cleaning reading
    NOTE: ADDED in CFX 1.5
    """
    
    # Bottom spray bars pressure reading, expressed in Pascals (Pa)
    BottomSprayBarsPressure = "BottomSprayBarsPressure"
    
    # Bottom water knife pressure reading, expressed in Pascals (Pa)
    BottomWaterKnifePressure = "BottomWaterKnifePressure"
    
    # Volume of cleaning chemistry added by the system, expressed in liter (l)
    CleaningChemistryVolumeAdd = "CleaningChemistryVolumeAdd"
    
    # min concentration reading, as a percentage from 0.0 to 100.0 (%)
    ConcentrationMin = "ConcentrationMin"
    
    # max concentration reading, as a percentage from 0.0 to 100.0 (%)
    ConcentrationMax = "ConcentrationMax"
    
    # average concentration reading, as a percentage from 0.0 to 100.0 (%)
    ConcentrationAverage = "ConcentrationAverage"
    
    # min conductivity reading, expressed in (uS/cm)
    ConductivityMin = "ConductivityMin"
    
    # max conductivity reading, expressed in (uS/cm)
    ConductivityMax = "ConductivityMax"
    
    # average conductivity reading, expressed in (uS/cm)
    ConductivityAverage = "ConductivityAverage"
    
    # Volume of DI water added by the system, expressed in liter (l)
    DIWaterVolumeAdd = "DIWaterVolumeAdd"
    
    # min flow rate reading, expressed in liter per minute (l/min)
    FlowRateMin = "FlowRateMin"
    
    # max flow rate reading, expressed in liter per minute (l/min)
    FlowRateMax = "FlowRateMax"
    
    # average flow rate reading, expressed in liter per minute (l/min)
    FlowRateAverage = "FlowRateAverage"
    
    # min liquid conductivity reading, expressed in (uS/cm)
    LiquidConductivityMin = "LiquidConductivityMin"
    
    # max liquid conductivity reading, expressed in (uS/cm)
    LiquidConductivityMax = "LiquidConductivityMax"
    
    # average liquid conductivity reading, expressed in (uS/cm)
    LiquidConductivityAverage = "LiquidConductivityAverage"
    
    # min liquid saturation reading, as a percentage from 0.0 to 100.0 (%)
    LiquidSaturationMin = "LiquidSaturationMin"
    
    # max liquid saturation reading, as a percentage from 0.0 to 100.0 (%)
    LiquidSaturationMax = "LiquidSaturationMax"
    
    # average liquid saturation reading, as a percentage from 0.0 to 100.0 (%)
    LiquidSaturationAverage = "LiquidSaturationAverage"
    
    # min liquid pressure reading, expressed in Pascals (Pa)
    PressureMin = "PressureMin"
    
    # max liquid pressure reading, expressed in Pascals (Pa)
    PressureMax = "PressureMax"
    
    # average liquid pressure reading, expressed in Pascals (Pa)
    PressureAverage = "PressureAverage"
    
    # amount of refresh water, expressed in liter (l)
    RefreshWaterAmount = "RefreshWaterAmount"
    
    # min temperature reading, expressed in degrees Celsius (C)
    TemperatureMin = "TemperatureMin"
    
    # max temperature reading, expressed in degrees Celsius (C)
    TemperatureMax = "TemperatureMax"
    
    # average temperature reading, expressed in degrees Celsius (C)
    TemperatureAverage = "TemperatureAverage"
    
    # Top spray bars pressure reading, expressed in Pascals (Pa)
    TopSprayBarsPressure = "TopSprayBarsPressure"
    
    # Top water knife pressure reading, expressed in Pascals (Pa)
    TopWaterKnifePressure = "TopWaterKnifePressure"
    
    # min ultrasonic power reading, expressed in Watt (W)
    UltrasonicPowerMin = "UltrasonicPowerMin"
    
    # max ultrasonic power reading, expressed in Watt (W)
    UltrasonicPowerMax = "UltrasonicPowerMax"
    
    # average ultrasonic power reading, expressed in Watt (W)
    UltrasonicPowerAverage = "UltrasonicPowerAverage"
    
    # vacuum reading, expressed in Pascals (Pa)
    Vacuum = "Vacuum"
    
    # frequency of Variable Frequency Drive, expressed in Hertz (Hz)
    VFDFrequency = "VFDFrequency"