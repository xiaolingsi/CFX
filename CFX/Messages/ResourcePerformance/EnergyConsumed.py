from dataclasses import dataclass, field
from typing import Optional, List

from dataclasses_json import dataclass_json

from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils


@dataclass_json
@dataclass
class EnergyConsumed(CFXMessage):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    EnergyUsed: float = 0.0
    PeakPower: float = 0.0
    MinimumPower: float = 0.0
    MeanPower: float = 0.0
    PowerNow: float = 0.0
    PowerFactorNow: float = 0.0
    PeakCurrent: float = 0.0
    MinimumCurrent: float = 0.0
    MeanCurrent: float = 0.0
    CurrentNow: float = 0.0
    PeakVoltage: float = 0.0
    MinimumVoltage: float = 0.0
    MeanVoltage: float = 0.0
    VoltageNow: float = 0.0
    PeakFrequency: float = 0.0
    MinimumFrequency: float = 0.0
    MeanFrequency: float = 0.0
    FrequencyNow: float = 0.0
    PeakPowerRYB: Optional[List[float]] = None
    MinimumPowerRYB: Optional[List[float]] = None
    MeanPowerRYB: Optional[List[float]] = None
    PowerNowRYB: Optional[List[float]] = None
    PowerFactorNowRYB: Optional[List[float]] = None
    PeakCurrentRYB: Optional[List[float]] = None
    MinimumCurrentRYB: Optional[List[float]] = None
    MeanCurrentRYB: Optional[List[float]] = None
    CurrentNowRYB: Optional[List[float]] = None
    PeakVoltageRYB: Optional[List[float]] = None
    MinimumVoltageRYB: Optional[List[float]] = None
    MeanVoltageRYB: Optional[List[float]] = None
    VoltageNowRYB: Optional[List[float]] = None
    ThreePhaseNeutralCurrentNow: float = 0.0

    def to_cfx_json(self):
        return self.to_json()

    def __init__(self, start_time=None, end_time=None, energy_used=0.0, peak_power=0.0, 
                 minimum_power=0.0, mean_power=0.0, power_now=0.0, power_factor_now=0.0,
                 peak_current=0.0, minimum_current=0.0, mean_current=0.0, current_now=0.0,
                 peak_voltage=0.0, minimum_voltage=0.0, mean_voltage=0.0, voltage_now=0.0,
                 peak_frequency=0.0, minimum_frequency=0.0, mean_frequency=0.0, frequency_now=0.0,
                 peak_power_ryb=None, minimum_power_ryb=None, mean_power_ryb=None, 
                 power_now_ryb=None, power_factor_now_ryb=None, peak_current_ryb=None,
                 minimum_current_ryb=None, mean_current_ryb=None, current_now_ryb=None,
                 peak_voltage_ryb=None, minimum_voltage_ryb=None, mean_voltage_ryb=None,
                 voltage_now_ryb=None, three_phase_neutral_current_now=0.0):
        super().__init__()
        self.type = "CFX.ResourcePerformance.EnergyConsumed,CFX"
        self.message_name = "CFX.ResourcePerformance.EnergyConsumed"
        self.StartTime = start_time if start_time is not None else CFXUtils.get_iso8601_time()
        self.EndTime = end_time if end_time is not None else CFXUtils.get_iso8601_time()
        self.EnergyUsed = energy_used
        self.PeakPower = peak_power
        self.MinimumPower = minimum_power
        self.MeanPower = mean_power
        self.PowerNow = power_now
        self.PowerFactorNow = power_factor_now
        self.PeakCurrent = peak_current
        self.MinimumCurrent = minimum_current
        self.MeanCurrent = mean_current
        self.CurrentNow = current_now
        self.PeakVoltage = peak_voltage
        self.MinimumVoltage = minimum_voltage
        self.MeanVoltage = mean_voltage
        self.VoltageNow = voltage_now
        self.PeakFrequency = peak_frequency
        self.MinimumFrequency = minimum_frequency
        self.MeanFrequency = mean_frequency
        self.FrequencyNow = frequency_now
        self.PeakPowerRYB = peak_power_ryb
        self.MinimumPowerRYB = minimum_power_ryb
        self.MeanPowerRYB = mean_power_ryb
        self.PowerNowRYB = power_now_ryb
        self.PowerFactorNowRYB = power_factor_now_ryb
        self.PeakCurrentRYB = peak_current_ryb
        self.MinimumCurrentRYB = minimum_current_ryb
        self.MeanCurrentRYB = mean_current_ryb
        self.CurrentNowRYB = current_now_ryb
        self.PeakVoltageRYB = peak_voltage_ryb
        self.MinimumVoltageRYB = minimum_voltage_ryb
        self.MeanVoltageRYB = mean_voltage_ryb
        self.VoltageNowRYB = voltage_now_ryb
        self.ThreePhaseNeutralCurrentNow = three_phase_neutral_current_now
