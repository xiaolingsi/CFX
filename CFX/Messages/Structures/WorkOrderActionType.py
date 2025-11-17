from enum import Enum


class WorkOrderActionType(Enum):
    """
    ** NOTE: ADDED in CFX 1.2 **
    Describes the type of action of a work order action.
    """
    
    # Activity does not fall into any of the pre-defined categories.
    Uncategorized = 0
    
    # The action is a recipe creation.
    RecipeCreation = 100
    
    # The action is a recipe modification.
    RecipeModification = 200
    
    # The action is a recipe optimization.
    RecipeOptimization = 300
    
    # The action is a pre production operation.
    PreProductionOperations = 400
    
    # The action is a pre production operation, related to material setup. Includes activities like feeder setup, paste application, etc.
    PreProductionOperations_MaterialSetup = 401
    
    # The action is a pre production operation, related to tooling setup. Includes setup type activities like stencil installation, etc.
    PreProductionOperations_ToolingSetup = 402
    
    # The action is a pre production operation, related to other types of setup.
    PreProductionOperations_OtherSetup = 403
    
    # The action is a pre production operation, related to quality checks, like first article runs and other quality pre-production activities.
    PreProductionOperations_QualityChecks = 404
    
    # The action is a post production operation. Includes breakdown, and other post-production activities.
    PostProductionOperations = 500
    
    # The action is a mid production operation.
    MidProductionOperations = 600
    
    # The action is a mid production operation, related to replenishment of materials, such as feeder resplenishment, new paste application, etc. 
    MidProcuctionOperations_MaterialReplenish = 601