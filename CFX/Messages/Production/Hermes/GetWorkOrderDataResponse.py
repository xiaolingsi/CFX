from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier
from CFX.Messages.Structures.Surface import Surface


@dataclass_json
@dataclass
class GetWorkOrderDataResponse(CFXMessage):
    Result: RequestResult
    WorkOrderIdentifier: WorkOrderIdentifier
    ProductTypeId: str
    Length: float
    Width: float
    Thickness: float
    TopClearanceHeight: float
    BottomClearanceHeight: float
    Weight: float
    Surface: Surface
    Route: int

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, work_order_identifier: WorkOrderIdentifier = None, 
                 product_type_id: str = "", length: float = 0.0, width: float = 0.0, 
                 thickness: float = 0.0, top_clearance_height: float = 0.0, 
                 bottom_clearance_height: float = 0.0, weight: float = 0.0, 
                 surface: Surface = Surface.Unspecified, route: int = 0):
        super().__init__()
        self.type = "CFX.Production.Hermes.GetWorkOrderDataResponse,CFX"
        self.message_name = "CFX.Production.Hermes.GetWorkOrderDataResponse"
        self.Result = result or RequestResult()
        self.WorkOrderIdentifier = work_order_identifier or WorkOrderIdentifier()
        self.ProductTypeId = product_type_id
        self.Length = length
        self.Width = width
        self.Thickness = thickness
        self.TopClearanceHeight = top_clearance_height
        self.BottomClearanceHeight = bottom_clearance_height
        self.Weight = weight
        self.Surface = surface
        self.Route = route
