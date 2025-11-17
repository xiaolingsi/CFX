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
from ..ComponentDesignator import ComponentDesignator
from ..Image import Image
from .PressTool import PressTool
from .PressProfile import PressProfile
from .ConnectorForces import ConnectorForces
from .Manufacturer import Manufacturer
from .Pars import Pars
from .SPC import SPC


@dataclass_json
@dataclass
class Connector(ComponentDesignator):
    """
    Describes a Pressed Connector
    """
    
    # Tool used to press this connector
    ConnectorTool: PressTool = field(default_factory=PressTool)
    
    # Profile used to press this connector
    ProfileApplied: PressProfile = field(default_factory=PressProfile)
    
    # The number of pins on this connector
    PinCount: int = 0
    
    # The image of this connector
    ConnectorImage: Image = field(default_factory=Image)
    
    # The dimesion of the top of the connector from the top of the board when the connector is not seated
    UnseatedTop: float = 0.0
    
    # The dimesion of the top of the connector from the top of the board when the connector is seated
    SeatedHeight: float = 0.0
    
    # The thickness of the connector
    BaseThickness: float = 0.0
    
    # Value to signfiy if the connector requires flatrock tooling (tooling that does not have openings for the pins)
    FlatrockTooling: bool = False
    
    # Connector force definitions
    Forces: ConnectorForces = field(default_factory=ConnectorForces)
    
    # Manufactuer of the connector
    ManufacturerData: Manufacturer = field(default_factory=Manufacturer)
    
    # Group identifier of the connector
    Group: str = ""
    
    # The pars setting
    ParsSetting: Pars = field(default_factory=Pars)
    
    # The SPC setting
    SPCSetting: SPC = field(default_factory=SPC)