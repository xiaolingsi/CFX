from dataclasses import dataclass
from dataclasses_json import dataclass_json
from CFX.CFXMessage import CFXMessage
from CFX.Messages.Structures.RequestResult import RequestResult
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.StationSetupRequirements import StationSetupRequirements


@dataclass_json
@dataclass
class GetRequiredSetupResponse(CFXMessage):
    Result: RequestResult
    RecipeName: str
    RecipeRevision: str
    Lane: int
    Stage: Stage
    SetupRequirements: StationSetupRequirements

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result: RequestResult = None, recipe_name: str = "", recipe_revision: str = "", 
                 lane: int = None, stage: Stage = None, setup_requirements: StationSetupRequirements = None):
        super().__init__()
        self.type = "CFX.Production.GetRequiredSetupResponse,CFX"
        self.message_name = "CFX.Production.GetRequiredSetupResponse"
        self.Result = result or RequestResult()
        self.RecipeName = recipe_name
        self.RecipeRevision = recipe_revision
        self.Lane = lane
        self.Stage = stage
        self.SetupRequirements = setup_requirements