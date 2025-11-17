from enum import Enum


class CalibrationType(Enum):
    """
    Types of calibrations
    """
    
    Unkwnown = "Unkwnown"
    General = "General"
    XAxis = "XAxis"
    YAxis = "YAxis"
    ZAxis = "ZAxis"
    UnitPosition = "UnitPosition"
    TravelRange = "TravelRange"
    SystemIdentification = "SystemIdentification"
    ZeroPointOffset = "ZeroPointOffset"
    BoardCamera = "BoardCamera"
    FeedUnitsTable = "FeedUnitsTable"
    NozzleChanger = "NozzleChanger"
    BoardReferenceCorner = "BoardReferenceCorner"
    ComponentSensorCamera = "ComponentSensorCamera"
    SegmentOffset = "SegmentOffset"
    ComponentSensorLightBarrier = "ComponentSensorLightBarrier"
    ZeroPressure = "ZeroPressure"
    BoardMapping = "BoardMapping"
    HeadMapping = "HeadMapping"
    HeadsAndCameras = "HeadsAndCameras"
    VacuumTooling = "VacuumTooling"