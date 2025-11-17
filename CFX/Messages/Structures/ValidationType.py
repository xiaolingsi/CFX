from enum import Enum


class ValidationType(Enum):
    """
    Types of validations
    """
    
    # A validation that ensures a unit is at the proper step in the route, and has completed all
    # pre-requisite steps.
    UnitRouteValidation = "UnitRouteValidation"
    
    # A validation that ensures a unit is not in a failed or error condition
    UnitStatusValidation = "UnitStatusValidation"
    
    # A validation that ensures a unit and ALL of its sub-assemblies are not in a failed or error condition
    UnitAndSubsStatusValidation = "UnitAndSubsStatusValidation"
    
    # Validates that the trace data has been recived for this unit from the sender by a factory level software system
    UnitTraceValidation = "UnitTraceValidation"
    
    # All known validations should be performed
    All = "All"