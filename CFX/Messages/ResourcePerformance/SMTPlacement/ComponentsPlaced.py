from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils


@dataclass_json
@dataclass
class ComponentsPlaced(CFXMessage):
    """
    Sent periodically by an SMT placement machine to indicate the number of placements which were
    successfully or unsuccessfully completed during the sample time window.
    This sample time window shall not exceed 10 minutes.
    """
    start_time: str = field(default_factory=CFXUtils.get_iso8601_time)
    end_time: str = field(default_factory=CFXUtils.get_iso8601_time)
    total_components_placed: int = 0
    total_components_not_placed: int = 0

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, start_time=None, end_time=None, total_components_placed=0, total_components_not_placed=0):
        super().__init__()
        self.type = "CFX.ResourcePerformance.SMTPlacement.ComponentsPlaced,CFX"
        self.message_name = "CFX.ResourcePerformance.SMTPlacement.ComponentsPlaced"
        self.start_time = start_time if start_time is not None else CFXUtils.get_iso8601_time()
        self.end_time = end_time if end_time is not None else CFXUtils.get_iso8601_time()
        self.total_components_placed = total_components_placed
        self.total_components_not_placed = total_components_not_placed