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
from .StepType import StepType


@dataclass_json
@dataclass
class ProfileStep:
    """
    Describes a individual step of a Press Profile
    """
    
    # The sequence position of this step in relation to the other steps in the profile.  Steps are peformed in increasing sequence integer order 1...n
    SequencePosition: int = 0
    
    # The name of this step
    Name: str = ""
    
    # The speed of this step in mm/s.
    Speed: float = 0.0
    
    # An enumeration indicating the type of this step
    TypeOfStep: StepType = StepType.MoveToHeightOrForce