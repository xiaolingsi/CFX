"""
Data specific to a single zone with the
Selective Soldering System
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from datetime import timedelta


@dataclass_json
@dataclass
class ZoneData:
    """
    Data specific to a single zone with the
    Selective Soldering System
    """
    
    # The identity of the zone for this set of process data.  
    # Corresponds to the StageSequence number of the related Stage
    StageSequence: int = 0
    
    # The time the item was within this zone
    # of the Selective Soldering System
    ProcessTime: Optional[timedelta] = "00:00:00"
    
    # Pressure of the Nitrogen for flux applicator 1
    # in kPa (kilopascal)
    Bottle1_Pressure: float = 0.0
    
    # Pressure of the Nitrogen for flux applicator 2
    # in kPa (kilopascal)
    Bottle2_Pressure: float = 0.0
    
    # The total volume of flux applied to the item
    # in mg (milligrams)
    Flux_Volume: float = 0.0
    
    # The power setting for the top side preheater
    # during the heating phase
    # as a percentage (0-100%)
    Top_Preheater_Power: float = 0.0
    
    # The power setting for the top side preheater
    # during the soak phase
    # as a percentage (0-100%)
    Top_Preheater_Soak: float = 0.0
    
    # The maximum temperature of the item
    # during the preheating cycle
    # in Celsius
    Top_Preheater_Temp: float = 0.0
    
    # The total time for the prehearting
    # phase within this zone
    Top_Preheater_Time: Optional[timedelta] = "00:00:00"
    
    # The power setting for the bottom side preheater
    # as a percentage (0-100%)        
    Bot_Preheater_Power: float = 0.0
    
    # The power setting for the bottom side preheater
    # during the soak phase
    # as a percentage (0-100%)
    Bot_Preheater_Soak: float = 0.0
    
    # The maximum temperature of the item
    # during the preheating cycle
    # in Celsius
    Bot_Preheater_Temp: float = 0.0
    
    # The total time for the prehearting
    # phase within this zone
    Bot_Preheater_Time: Optional[timedelta] = "00:00:00"
    
    # Temperature of the solder bath
    # in Celsius
    Bath_Temp: float = 0.0
    
    # Solder Wave Height correction enabled 
    # for the selective soldering system
    # "True" or "False"
    Bath_Wave_Enabled: bool = False
    
    # The value the wave height was corrected by
    # in mm (millimetres)
    Bath_Wave_Hgt: float = 0.0
    
    # The quantity of solder consumed by the soldering process
    # in grams
    Solder_Quantity_Used: float = 0.0
    
    # The X-axis fiducial correction value
    # in mm (millimetres)
    Fid_XCorrection: float = 0.0
    
    # The Y-axis fiducial correction value
    # in mm (millimetres)
    Fid_YCorrection: float = 0.0