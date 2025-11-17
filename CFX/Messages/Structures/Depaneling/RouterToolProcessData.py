from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from decimal import Decimal
from dataclasses_json import dataclass_json
from CFX.Messages.Structures.ProcessData import ProcessData
from CFX.Messages.Structures.Depaneling.Axis import Axis


@dataclass_json
@dataclass
class RouterToolProcessData(ProcessData):
    """
    Provides information about the processing conditions for a depaneling machine at the time when a unit was processed.
    NOTE: ADDED in CFX 1.5
    """
    
    # Tool Data -Version
    ToolDataVersion: Decimal = Decimal("0.0")
    
    # Machine set point Value- tool bit diameter (in mm)
    ToolDiameter_SetPoint: Decimal = Decimal("0.0")
    
    # Tool bit start used time
    ToolBitStartTime: datetime = datetime.min
    
    # Last Tool bit stop used time
    ToolBitEndTime: datetime = datetime.min
    
    # Distance of ALL tabs cut since last Bit Change 
    ToolBitDistanceRouted: Decimal = Decimal("0.0")
    
    # Alarm set to optimal distance for bit change
    ToolBitChangeDistanceAlarmSet: Decimal = Decimal("0.0")
    
    # Panel count for batch/period routed
    NumberOfBoardsRouted: int = 0
    
    # Machine set point - feed rate routing program (in mm/s)
    FeedRate_SetPoint: Decimal = Decimal("0.0")
    
    # Distance of ALL tabs cut since last bag/filter change in (in Meter).
    VacuumDistanceRouted: Decimal = Decimal("0.0")
    
    # Alarm set to optimal distance for filter change in (Meter).
    VacuumFilterChangeDistanceAlarmSet: Decimal = Decimal("0.0")
    
    # Vacuum or Negative Pressure Level
    ActualVacuumLevel: Decimal = Decimal("0.0")
    
    # Incoming Air Pressure Level
    ActualIncomingPressure: Decimal = Decimal("0.0")
    
    # Electric Power consumption of Machine
    ActualMachinePower: Decimal = Decimal("0.0")
    
    # Max gripper force applied to PCB. (N)(Optional only-Applicable for gripper hardware equipment type)
    ActualGripperForcePickAndPlace: Decimal = Decimal("0.0")
    
    # Machine set point – Spindle Speed (in mm/s)
    SpindleSpeed_SetPoint: Decimal = Decimal("0.0")
    
    # Min Speed at which the Spindle operates - RPM (Revolutions per minute)
    MinSpindleRpm: Decimal = Decimal("0.0")
    
    # Max Speed at which the Spindle operates - RPM (Revolutions per minute)
    MaxSpindleRpm: Decimal = Decimal("0.0")
    
    # List of Axis for Router
    AxisDetails: List[Axis] = field(default_factory=list)
    
    def __init__(self, toolDataVersion=Decimal("0.0"), toolDiameter_SetPoint=Decimal("0.0"),
                 toolBitStartTime=datetime.min, toolBitEndTime=datetime.min,
                 toolBitDistanceRouted=Decimal("0.0"), toolBitChangeDistanceAlarmSet=Decimal("0.0"),
                 numberOfBoardsRouted=0, feedRate_SetPoint=Decimal("0.0"),
                 vacuumDistanceRouted=Decimal("0.0"), vacuumFilterChangeDistanceAlarmSet=Decimal("0.0"),
                 actualVacuumLevel=Decimal("0.0"), actualIncomingPressure=Decimal("0.0"),
                 actualMachinePower=Decimal("0.0"), actualGripperForcePickAndPlace=Decimal("0.0"),
                 spindleSpeed_SetPoint=Decimal("0.0"), minSpindleRpm=Decimal("0.0"),
                 maxSpindleRpm=Decimal("0.0"), axisDetails=None):
        super().__init__()
        self.ToolDataVersion = toolDataVersion
        self.ToolDiameter_SetPoint = toolDiameter_SetPoint
        self.ToolBitStartTime = toolBitStartTime
        self.ToolBitEndTime = toolBitEndTime
        self.ToolBitDistanceRouted = toolBitDistanceRouted
        self.ToolBitChangeDistanceAlarmSet = toolBitChangeDistanceAlarmSet
        self.NumberOfBoardsRouted = numberOfBoardsRouted
        self.FeedRate_SetPoint = feedRate_SetPoint
        self.VacuumDistanceRouted = vacuumDistanceRouted
        self.VacuumFilterChangeDistanceAlarmSet = vacuumFilterChangeDistanceAlarmSet
        self.ActualVacuumLevel = actualVacuumLevel
        self.ActualIncomingPressure = actualIncomingPressure
        self.ActualMachinePower = actualMachinePower
        self.ActualGripperForcePickAndPlace = actualGripperForcePickAndPlace
        self.SpindleSpeed_SetPoint = spindleSpeed_SetPoint
        self.MinSpindleRpm = minSpindleRpm
        self.MaxSpindleRpm = maxSpindleRpm
        self.AxisDetails = axisDetails if axisDetails is not None else []