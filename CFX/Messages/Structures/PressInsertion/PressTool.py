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
from ..Tool import Tool


@dataclass_json
@dataclass
class PressTool(Tool):
    """
    Represents a type of tool used in press insertion operations
    """
    
    # The x dimension of the tool used for the pressing operation
    ToolDimensionX: float = 0.0
    
    # The y dimension of the tool used for the pressing operation
    ToolDimensionY: float = 0.0
    
    # The z dimension of the tool used for the pressing operation
    ToolDimensionZ: float = 0.0
    
    # The clearance dimension of the tool used for the pressing operation
    ToolClearanceDimension: float = 0.0