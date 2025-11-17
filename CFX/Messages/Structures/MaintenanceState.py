from enum import Enum

class MaintenanceState(Enum):
    """Possible Maintenance status. It is used in the response message, after 
    the endpoint / resource has sent a status info request"""
    
    # Maintenance status is not known
    Unknown = "Unknown"
    # Maintenance status is Ok
    Ok = "Ok"
    # Maintenance status is Not ok
    NotOk = "NotOk"