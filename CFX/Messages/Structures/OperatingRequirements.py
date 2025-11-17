from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class OperatingRequirements:
    """Structure that specifies the operating requirements (environmental, etc.) 
    of a given endpoint."""
    
    # The minimum level of relative humidity (expressed as a percentage from 0 to 1) required
    # for the endpoint to operate
    MinimumHumidity: float = 0.0
    
    # The maximum level of relative humidity (expressed as a percentage from 0 to 1) that the
    # endpoint can tolerate
    MaximumHumidity: float = 0.0
    
    # The minimum templerature (expressed in degrees Celsius) required
    # for the endpoint to operate
    MinimumTemperature: float = 0.0
    
    # The maximum templerature (expressed in degrees Celsius) that the endpoint can tolerate.
    MaximumTemperature: float = 0.0