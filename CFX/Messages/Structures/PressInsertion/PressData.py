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
class PressData:
    """
    Describes various data pertaining the result of a press.
    """
    
    # Status indicating how the press terminated
    Status: str = ""
    
    # Describes the force or height measurement which caused the press to terminate
    TerminationMeasurement: str = ""
    
    # The average force measured over the SPC position range
    SPCAverageForce: float = 0.0
    
    # The height at which max pressing force was achieved
    HeightAtMaxForce: float = 0.0
    
    # The max force achieved during the press
    MaxForce: float = 0.0
    
    # The height at which the press terminated
    TerminationHeight: float = 0.0
    
    # The force at which the press terminated
    TerminationForce: float = 0.0