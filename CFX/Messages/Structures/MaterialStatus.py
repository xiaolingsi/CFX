from enum import Enum

class MaterialStatus(Enum):
    """Status of a material package"""
    
    # Material is available for use in production
    Active = "Active"
    # Material has been blocked, and should not be used in production
    Blocked = "Blocked"
    # Material has been exhausted, and can no longer be used in production
    Depleted = "Depleted"