from enum import Enum

class PerformanceImpactCause(Enum):
    """** NOTE: ADDED in CFX 1.6 **
    Possible causes of lower-than-expected performance, which a machine may be able to report as performance impacts"""
    
    # An alternative track was used for component pick-up
    AlternativeTrackUsed = "AlternativeTrackUsed"
    # A segment on a head was deactivated
    DeactivatedSegmentOnHead = "DeactivatedSegmentOnHead"
    # Option "Dump Always" activated for vision system
    VisionSystemDumpAlwaysActivated = "VisionSystemDumpAlwaysActivated"
    # Vision system had to acquire additional images
    AdditionalImageAcquisition = "AdditionalImageAcquisition"
    # Feeder speed is lower than expected
    LowFeederSpeed = "LowFeederSpeed"
    # Gang pick head cannot pick in parallel
    GangPickNoParallelPick = "GangPickNoParallelPick"