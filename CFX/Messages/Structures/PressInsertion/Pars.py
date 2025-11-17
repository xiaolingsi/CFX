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


@dataclass_json
@dataclass
class Pars:
    """
    A connector can be pressed with force that iproportional to the 
    actual resisting force detected during the pressing cycle.We call 
    this Percent Above Range Sample, or PARS.In this technique, 
    the connector's resisting force while pressing is
    sampled and averaged over a distance range above final seating to 
    the board surface. The final force percent added assures complete 
    seating of the connector.This is the most widely used technique
    because it limits the stress to the assembly, but does not require 
    great accuracy for board thickness measurement.
    """
    
    # Gets or sets the percent above the sample range.
    PercentAbove: float = 0.0
    
    # Gets or sets the start height in mm.
    StartHeight: float = 0.0
    
    # Gets or sets the distance in mm
    Distance: float = 0.0