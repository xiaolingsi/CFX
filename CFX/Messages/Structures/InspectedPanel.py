from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, List
from CFX.Messages.Structures.InspectedUnit import InspectedUnit


@dataclass_json
@dataclass
class InspectedPanel(object):
    """
    Describes an inspected panel
    """
    
    # 需要从C#源码中获取具体属性，这里先创建基础结构
    pass