from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier


@dataclass_json
@dataclass
class HermesUnit(object):
    """
    Structure that contains information related to a Unit (Board) according to the Hermes standard.
    """
    
    SlotId: int = 0
    BoardId: Optional[str] = None
    BoardIdCreatedBy: Optional[str] = None
    FailedBoard: int = 0
    ProductTypeId: Optional[str] = None
    FlippedBoard: int = 0
    TopBarcode: Optional[str] = None
    BottomBarcode: Optional[str] = None
    Lenght: Optional[float] = None
    Width: Optional[float] = None
    Thickness: Optional[float] = None
    ConveyorSpeed: Optional[float] = None
    TopClearanceHeight: Optional[float] = None
    BottomClearanceHeight: Optional[float] = None
    Weight: Optional[float] = None
    WorkOrderIdentifier: Optional[WorkOrderIdentifier] = None