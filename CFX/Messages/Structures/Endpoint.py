from dataclasses import dataclass
from dataclasses_json import dataclass_json

from CFX.CFXUtils import CFXUtils
from CFX.Messages.Structures.HermesInformation import HermesInformation
from CFX.Messages.Structures.OperatingRequirements import OperatingRequirements
from CFX.Messages.Structures.OperatingSystem import OperatingSystem
from CFX.Messages.Structures.OperatingSystemPlatform import OperatingSystemPlatform
from CFX.Messages.Structures.DimensionalConstraints import DimensionalConstraints
from CFX.Messages.Structures.StageInformation import StageInformation
from CFX.Messages.genericUnits.SupportedTopic import SupportedTopic


@dataclass_json
@dataclass
class Endpoint(object):
    CFXHandle: str
    CFXVersion: str
    FirmwareVersion: str
    FriendlyName: str
    # HermesInformation: HermesInformation
    ModelNumber: str
    NumberOfLanes: int
    # OperatingRequirements: OperatingRequirements
    # OperatingSystem: OperatingSystem
    # OperatingSystemPlatform: OperatingSystemPlatform
    OperatingSystemVersion: str
    RequestNetworkUri: str
    RequestTargetAddress: str
    SerialNumber: str
    SleepStates: list
    SoftwareVersion: str
    Stages: list
    # SupportedPCBDimensions: DimensionalConstraints
    SupportedTopics: list
    UniqueIdentifier: str
    Vendor: str

    def __init__(self,handle="",modelNumber ="",numberOfLanes=0,requestNetworkUri="",requestTargetAddress="",
                serialNumber ="",uniqueIdentifie="",vendor=""):
        self.CFXHandle = handle
        self.ModelNumber = modelNumber
        self.NumberOfLanes = numberOfLanes
        self.RequestNetworkUri = requestNetworkUri
        self.RequestTargetAddress = requestTargetAddress
        self.SerialNumber = serialNumber
        self.UniqueIdentifier = uniqueIdentifie
        self.Vendor = vendor
        self.Stages = list()
        self.SupportedTopics = list()
        self.CFXVersion = CFXUtils.get_cfx_version()
        self.FirmwareVersion = ""
        self.FriendlyName = ""
        self.OperatingSystemVersion = ""
        self.SleepStates = []
        self.SoftwareVersion = ""
        self.HermesInformation = None




    def add_stage(self,stageInformation:StageInformation):
        self.Stages.append(stageInformation)

    def add_support_topic(self,supportTopic:SupportedTopic):
        self.SupportedTopics.append(supportTopic)

