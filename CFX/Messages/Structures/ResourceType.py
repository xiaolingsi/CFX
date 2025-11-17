from enum import Enum

class ResourceType(Enum):
    """** NOTE: ADDED in CFX 1.7 **
    Describes a resource type"""
    
    # Unknown resource type
    Unknown = "Unknown"
    # The resource is a machine, also known as a "process endpoint"
    Machine = "Machine"
    # The resource is a shelf, with no intelligence
    Shelf = "Shelf"
    # The resource is a storage tower, with a potential intelligence and a specific way of classifying materials
    StorageTower = "StorageTower"
    # The resource is a setup station (typically a PC with material programming capabilities)
    SetupStation = "SetupStation"
    # The resource is a storage room
    StorageRoom = "StorageRoom"
    # The resource is a waiting area, i.e a setup area
    WaitingArea = "WaitingArea"