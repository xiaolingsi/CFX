from enum import Enum


class SamplingMethod(Enum):
    """
    Describes a particular sampling methodology.
    """
    
    # No sampling.  All units are inspected (100% Inspection).
    NoSampling = "NoSampling"
    
    # Units sampled according to ANSI/ASQ Z1.4 AQL methods.
    ANSI_Z14 = "ANSI_Z14"
    
    # Units sampled according to MIL-STD-105 mil standard.
    MIL_STD_105 = "MIL_STD_105"
    
    # Units sampled according to MIL-STD-1916 mil standard.
    MIL_STD_1916 = "MIL_STD_1916"
    
    # Units sampled according to the Squeglia AQL method.
    Squeglia = "Squeglia"
    
    # A fixed number of units were sampled (lot size disregarded).
    FixedSample = "FixedSample"