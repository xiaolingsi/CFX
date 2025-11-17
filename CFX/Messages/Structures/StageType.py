from enum import Enum


class StageType(Enum):
    """
    An enumeration indicating different types of stages that might exist at an endpoint.
    """
    
    # Work on production units is performed at this stage.  This may be any sort of work, including assembly, inspection, processing, etc.
    Work = "Work"
    
    # This stage is intended to serve as a buffer for production units.  No work is performed at this stage.
    Buffer = "Buffer"