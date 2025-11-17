from enum import Enum


class HazardousMaterialType(Enum):
    """
    Specifies whether or not a material is hazardous, and if so, the regulatory directive that controls
    the use of this substance in production.
    """
    
    NotHazardous = "NotHazardous"
    Hazardous = "Hazardous"
    RoHS = "RoHS"