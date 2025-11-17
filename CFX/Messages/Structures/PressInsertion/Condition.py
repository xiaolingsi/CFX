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
from .ConditionStep import ConditionStep


@dataclass_json
@dataclass
class Condition:
    """
    Describes a Condition Sequence.  Conditions consist of one or more steps that control non-pressing actions for a press recipe.
    """
    
    # The name of the condition.
    ConditionName: str = ""
    
    # An array of the steps of the Condition.
    Steps: List[ConditionStep] = field(default_factory=list)
    
    # String containing the aggregated JavaScript code of all condition steps.
    JavaScriptCode: str = ""
    
    # Indicates whether condition is a single step or consists of multiple sub-steps
    MultiStep: bool = False