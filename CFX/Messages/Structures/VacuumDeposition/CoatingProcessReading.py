from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .. import Reading

@dataclass_json
@dataclass
class CoatingProcessReading(Reading):
    """
    Structure base class representing process data.
    Chamber pressure units in mbar.
    Vaporizer temperature in degrees Celsius.
    ** NOTE: ADDED in CFX 1.2 **
    """
    chamber_pressure: float
    vaporizer_temperature: float