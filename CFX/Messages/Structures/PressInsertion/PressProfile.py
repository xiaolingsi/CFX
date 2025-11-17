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
from .ProfileStep import ProfileStep


@dataclass_json
@dataclass
class PressProfile:
    """
    Describes a Press Profile.  Press Profile consist of a sequence of steps which describe the motion of the pressing operation.
    """
    
    # The name of the profile.
    ProfileName: str = ""
    
    # An array of the steps of the Press Profile.
    Steps: List[ProfileStep] = field(default_factory=list)