from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from CFX.Messages.Structures.Head import Head


@dataclass_json
@dataclass
class HeadInformation(object):
    """
    Describes a particular head of an automated endpoint that uses one or more heads in the course of its work.
    """
    
    Head: Optional[Head] = None