"""
Copyright 2018 TE Connectivity

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-------------------------------------------------------------------------
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from datetime import datetime
from ..ProcessData import ProcessData
from ..TestResult import TestResult
from ..SolderReflow.ReflowZoneData import ReflowZoneData


@dataclass_json
@dataclass
class ReflowProfilingProcessData(ProcessData):
    """
    Provides production unit reflow statistics
    """
    
    # Time and date Production Unit entered oven in ISO 8061 Datetime format.
    TimeDateUnitIn: datetime = field(default_factory=datetime.now)
    
    # Time and date Production Unit exited oven in short date pattern.
    TimeDateUnitOut: datetime = field(default_factory=datetime.now)
    
    # Name of product
    ProductName: str = ""
    
    # Barcode of Production Unit
    Barcode: str = ""
    
    # Name of recipe
    RecipeName: str = ""
    
    # Name of process window
    ProcessWindowName: str = ""
    
    # Lot identification value
    LotID: str = ""
    
    # Name of oven
    OvenName: str = ""
    
    # Lane within oven. 1 is "front" and 2 is "back"
    Lane: int = 1
    
    # The converyor speed setpoint (in cm / minute)
    ConveyorSpeedSetpoint: float = 0.0
    
    # The actual conveyor speed (in cm / minute)
    MeasuredConveyorSpeed: float = 0.0
    
    # "PASS" or "FAIL". FAIL if absolute value of ProductionUnitPWI exceeds 100.0
    Result: TestResult = TestResult.Passed
    
    # The Process Window Index of the production unit
    ProductionUnitPWI: float = 0.0
    
    # Process data (temperatures, etc.) for each zone of the reflow oven at the
    # time when this transaction tool place.
    ZoneData: List[ReflowZoneData] = field(default_factory=list)