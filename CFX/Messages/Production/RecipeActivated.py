from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List, Optional
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.WorkOrderIdentifier import WorkOrderIdentifier
from CFX.Messages.Structures.Surface import Surface
from CFX.Messages.Structures.RecipeStageInformation import RecipeStageInformation


@dataclass_json
@dataclass
class RecipeActivated(CFXMessage):
    RecipeName: Optional[str] = None
    Revision: Optional[str] = None
    Lane: Optional[int] = 0
    Stage: Optional[Stage] = None
    ExpectedCycleTime: Optional[float] = 0.0
    ExpectedWorkTime: Optional[float] = 0.0
    ExpectedUnitsPerWorkTransaction: Optional[float] = 0.0
    NumberOfComponentsPerUnit: Optional[float] = 0.0
    WorkOrderIdentifier: Optional[WorkOrderIdentifier] = None
    TargetQuantity: Optional[float] = 0.0
    RelevantSurface: Optional[Surface] = None
    RecipeStagesInformation: Optional[List[RecipeStageInformation]] = None

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, recipe_name: str = "", revision: str = "", lane: int = None, stage: Stage = None, 
                 expected_cycle_time: float = 0.0, expected_work_time: float = None, 
                 expected_units_per_work_transaction: float = 0.0, number_of_components_per_unit: float = 0.0,
                 work_order_identifier: WorkOrderIdentifier = None, target_quantity: float = 0.0,
                 relevant_surface: Surface = None, recipe_stages_information: List[RecipeStageInformation] = None):
        super().__init__()
        self.type = "CFX.Production.RecipeActivated,CFX"
        self.message_name = "CFX.Production.RecipeActivated"
        self.RecipeName = recipe_name
        self.Revision = revision
        self.Lane = lane
        self.Stage = stage
        self.ExpectedCycleTime = expected_cycle_time
        self.ExpectedWorkTime = expected_work_time
        self.ExpectedUnitsPerWorkTransaction = expected_units_per_work_transaction
        self.NumberOfComponentsPerUnit = number_of_components_per_unit
        self.WorkOrderIdentifier = work_order_identifier
        self.TargetQuantity = target_quantity
        self.RelevantSurface = relevant_surface or Surface.Unspecified
        self.RecipeStagesInformation = recipe_stages_information or []