from enum import Enum


class UninstalledReason(Enum):
    """
    Reason why a component or material was uninstalled from a production unit
    """
    
    # The component or material was defective, and had to be replaced.
    DefectiveMaterial = "DefectiveMaterial"
    
    # The component or material was not installed correctly, and had to be replaced or re-installed
    DefectiveInstallation = "DefectiveInstallation"
    
    # The wrong component or material was installed, and had to be replaced.
    IncorrectMaterial = "IncorrectMaterial"
    
    # The component or material was uninstalled for a reason not covered by this enumeration.
    Other = "Other"