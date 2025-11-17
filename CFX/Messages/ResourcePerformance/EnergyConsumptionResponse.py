from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional

from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.RequestResult import RequestResult


@dataclass_json
@dataclass
class EnergyConsumptionResponse(CFXMessage):
    """
    Response to an external source inquiring data regarding energy consumption of the endpoint.
    ** NOTE: ADDED in CFX 1.3 **
    """
    result: RequestResult = field(default_factory=RequestResult)
    start_time: str = field(default_factory=CFXUtils.get_iso8601_time)
    end_time: str = field(default_factory=CFXUtils.get_iso8601_time)
    energy_used: float = 0.0
    peak_power: float = 0.0
    minimum_power: float = 0.0
    mean_power: float = 0.0
    power_now: float = 0.0
    power_factor_now: float = 0.0
    peak_current: float = 0.0
    minimum_current: float = 0.0
    mean_current: float = 0.0
    current_now: float = 0.0
    peak_voltage: float = 0.0
    minimum_voltage: float = 0.0
    mean_voltage: float = 0.0
    voltage_now: float = 0.0
    peak_frequency: float = 0.0
    minimum_frequency: float = 0.0
    mean_frequency: float = 0.0
    frequency_now: float = 0.0
    peak_power_ryb: Optional[List[float]] = None
    minimum_power_ryb: Optional[List[float]] = None
    mean_power_ryb: Optional[List[float]] = None
    power_now_ryb: Optional[List[float]] = None
    power_factor_now_ryb: Optional[List[float]] = None
    peak_current_ryb: Optional[List[float]] = None
    minimum_current_ryb: Optional[List[float]] = None
    mean_current_ryb: Optional[List[float]] = None
    current_now_ryb: Optional[List[float]] = None
    peak_voltage_ryb: Optional[List[float]] = None
    minimum_voltage_ryb: Optional[List[float]] = None
    mean_voltage_ryb: Optional[List[float]] = None
    voltage_now_ryb: Optional[List[float]] = None
    three_phase_neutral_current_now: float = 0.0

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, result=None, start_time=None, end_time=None, energy_used=0.0, 
                 peak_power=0.0, minimum_power=0.0, mean_power=0.0, power_now=0.0, 
                 power_factor_now=0.0, peak_current=0.0, minimum_current=0.0, 
                 mean_current=0.0, current_now=0.0, peak_voltage=0.0, minimum_voltage=0.0, 
                 mean_voltage=0.0, voltage_now=0.0, peak_frequency=0.0, minimum_frequency=0.0, 
                 mean_frequency=0.0, frequency_now=0.0, peak_power_ryb=None, 
                 minimum_power_ryb=None, mean_power_ryb=None, power_now_ryb=None, 
                 power_factor_now_ryb=None, peak_current_ryb=None, minimum_current_ryb=None, 
                 mean_current_ryb=None, current_now_ryb=None, peak_voltage_ryb=None, 
                 minimum_voltage_ryb=None, mean_voltage_ryb=None, voltage_now_ryb=None, 
                 three_phase_neutral_current_now=0.0):
        super().__init__()
        self.type = "CFX.ResourcePerformance.EnergyConsumptionResponse,CFX"
        self.message_name = "CFX.ResourcePerformance.EnergyConsumptionResponse"
        self.result = result if result is not None else RequestResult()
        self.start_time = start_time if start_time is not None else CFXUtils.get_iso8601_time()
        self.end_time = end_time if end_time is not None else CFXUtils.get_iso8601_time()
        self.energy_used = energy_used
        self.peak_power = peak_power
        self.minimum_power = minimum_power
        self.mean_power = mean_power
        self.power_now = power_now
        self.power_factor_now = power_factor_now
        self.peak_current = peak_current
        self.minimum_current = minimum_current
        self.mean_current = mean_current
        self.current_now = current_now
        self.peak_voltage = peak_voltage
        self.minimum_voltage = minimum_voltage
        self.mean_voltage = mean_voltage
        self.voltage_now = voltage_now
        self.peak_frequency = peak_frequency
        self.minimum_frequency = minimum_frequency
        self.mean_frequency = mean_frequency
        self.frequency_now = frequency_now
        self.peak_power_ryb = peak_power_ryb
        self.minimum_power_ryb = minimum_power_ryb
        self.mean_power_ryb = mean_power_ryb
        self.power_now_ryb = power_now_ryb
        self.power_factor_now_ryb = power_factor_now_ryb
        self.peak_current_ryb = peak_current_ryb
        self.minimum_current_ryb = minimum_current_ryb
        self.mean_current_ryb = mean_current_ryb
        self.current_now_ryb = current_now_ryb
        self.peak_voltage_ryb = peak_voltage_ryb
        self.minimum_voltage_ryb = minimum_voltage_ryb
        self.mean_voltage_ryb = mean_voltage_ryb
        self.voltage_now_ryb = voltage_now_ryb
        self.three_phase_neutral_current_now = three_phase_neutral_current_now