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
class SPC:
    """
    Statistial Process Control parameters for the pressing operation.
    """
    
    # Gets or sets the distance from the board when SPC will be initiated
    StartDistance: float = 0.0
    
    # Gets or sets the start height.
    StartHeight: float = 0.0
    
    # Gets or sets the minimum force limit per pin (N/pin).
    MinimumForceLimit: float = 0.0
    
    # Gets or sets the maximum force limit per pin (N/pin)
    MaximumForceLimit: float = 0.0