import asyncio

from Amqp.CFXContainer import CFXContainer
from Amqp.CFXEndpoint import CFXEndpoint
from CFX.CFXEnvelope import CFXEnvelope
from CFX.CFXMessage import CFXMessage
from CFX.Messages.CoreCommunication.AreYouThereRequest import AreYouThereRequest
from CFX.Messages.CoreCommunication.AreYouThereResponse import AreYouThereResponse
from CFX.Messages.CoreCommunication.GetEndpointInformationResponse import GetEndpointInformationResponse
from CFX.Messages.CoreCommunication.WhoIsThereRequest import WhoIsThereRequest
from CFX.Messages.CoreCommunication.WhoIsThereResponse import WhoIsThereResponse
from CFX.Messages.CoreCommunication.EndpointConnected import EndpointConnected
from CFX.Messages.CoreCommunication.EndpointShuttingDown import EndpointShuttingDown
from CFX.Messages.Information.UnitValidation.ValidateUnitsRequest import ValidateUnitsRequest
from CFX.Messages.Production.GetActiveRecipeRequest import GetActiveRecipeRequest
from CFX.Messages.Production.GetActiveRecipeResponse import GetActiveRecipeResponse
from CFX.Messages.Production.RecipeActivated import RecipeActivated
from CFX.Messages.Production.RecipeModified import RecipeModified
from CFX.Messages.ResourcePerformance.FaultAcknowledged import FaultAcknowledged
from CFX.Messages.ResourcePerformance.FaultCleared import FaultCleared
from CFX.Messages.ResourcePerformance.FaultOccurred import FaultOccurred
from CFX.Messages.ResourcePerformance.GetActiveFaultsResponse import GetActiveFaultsResponse
from CFX.Messages.ResourcePerformance.HandleFaultResponse import HandleFaultResponse
from CFX.Messages.ResourcePerformance.LogEntryRecorded import LogEntryRecorded
from CFX.Messages.ResourcePerformance.ModifyStationParametersResponse import ModifyStationParametersResponse
from CFX.Messages.ResourcePerformance.StationOffline import StationOffline
from CFX.Messages.ResourcePerformance.StationOnline import StationOnline
from CFX.Messages.ResourcePerformance.StationParametersModified import StationParametersModified
from CFX.Messages.ResourcePerformance.StationStateChanged import StationStateChanged
from CFX.Messages.Structures.Endpoint import Endpoint
from CFX.Messages.Structures.Fault import Fault
from CFX.Messages.Structures.GenericParameter import GenericParameter
from CFX.Messages.Structures.Operator import Operator
from CFX.Messages.Structures.ResourceState import ResourceState
from CFX.Messages.Structures.StageInformation import StageInformation
from CFX.Messages.Structures.Stage import Stage
from CFX.Messages.Structures.UnitPosition import UnitPosition
from CFX.Messages.genericUnits.RequestResult import RequestResult
from CFX.Messages.genericUnits.StageType import StageType
from CFX.Messages.genericUnits.StatusResult import StatusResult
from CFX.Messages.genericUnits.SupportedTopic import SupportedTopic
from CFX.Messages.genericUnits.SupportedTopicQueryType import SupportedTopicQueryType
from CFX.Messages.genericUnits.WorkResult import WorkResult
from CFX.Messages.genericUnits.WorkStagePauseReason import WorkStagePauseReason
from CFX.Messages.wip.UnitsArrived import UnitsArrived
from CFX.Messages.wip.UnitsDeparted import UnitsDeparted
from CFX.Messages.wip.WorkCompleted import WorkCompleted
from CFX.Messages.wip.WorkStageCompleted import WorkStageCompleted
from CFX.Messages.wip.WorkStagePaused import WorkStagePaused
from CFX.Messages.wip.WorkStageResumed import WorkStageResumed
from CFX.Messages.wip.WorkStageStarted import WorkStageStarted
from CFX.Messages.wip.WorkStart import WorkStarted


class MyCFXEndpoint(CFXEndpoint):

    def __init__(self, local_url, cfx_handle):
        super(MyCFXEndpoint, self).__init__(local_url, cfx_handle)
        self.log_utils.set_log_path("../CFX/Log")

    def on_message_receive_from_listener(self, msg) -> None:
        self.log_utils.info_log("Message receive from listener")
        self.log_utils.info_log(msg)

    def on_request_receive(self, request) -> [dict, None, CFXMessage]:
        self.log_utils.info_log("Request receive")
        self.log_utils.info_log(request)
        if request["MessageName"] == "CFX.AreYouThereRequest":
            resp_msg = CFXEnvelope(message_body=AreYouThereResponse(self.cfx_handle, self.local_url, self.cfx_handle))
            return resp_msg.to_json()
        elif request["MessageName"] == "CFX.WhoIsThereRequest":
            resp_msg = CFXEnvelope(message_body=WhoIsThereResponse(self.cfx_handle, self.local_url, self.cfx_handle))
            return resp_msg.to_json()
        elif request["MessageName"] == "CFX.GetEndpointInformationRequest":
            endpoint_information = Endpoint(self.cfx_handle, "sadfgh")
            endpoint_information.add_stage(StageInformation(Stage()))
            endpoint_information.add_stage(StageInformation(Stage()))
            endpoint_information.add_support_topic(SupportedTopic())
            request_result = RequestResult(StatusResult.Success, 0, "Success")
            getEndpointInformationResponse = GetEndpointInformationResponse(endpoint_information, request_result)
            resp_msg = CFXEnvelope(message_body=getEndpointInformationResponse)
            return resp_msg.to_json()
        elif request["MessageName"] == "CFX.Production.GetActiveRecipeRequest":
            request_result = RequestResult(StatusResult.Success, 0, "Success")
            resp = GetActiveRecipeResponse(result=request_result, active_recipe_name="aaaa",
                                           active_recipe_revision="212")
            resp_msg = CFXEnvelope(message_body=resp)
            return resp_msg.to_json()
        elif request["MessageName"] == "CFX.ResourcePerformance.HandleFaultRequest":
            request_result = RequestResult(StatusResult.Success, 0, "Success")
            resp = HandleFaultResponse(result=request_result)
            resp_msg = CFXEnvelope(message_body=resp)
            return resp_msg.to_json()
        elif request["MessageName"] == "CFX.ResourcePerformance.GetActiveFaultsRequest":
            request_result = RequestResult(StatusResult.Success, 0, "Success")
            resp = GetActiveFaultsResponse(result=request_result)
            resp.add_fault(Fault(description="ERROR", fault_code="123"))
            resp_msg = CFXEnvelope(message_body=resp)
            return resp_msg.to_json()
        elif request["MessageName"] == "CFX.ResourcePerformance.ModifyStationParametersRequest":
            request_result = RequestResult(StatusResult.Success, 0, "Success")
            resp = ModifyStationParametersResponse(result=request_result)
            resp_msg = CFXEnvelope(message_body=resp)
            return resp_msg.to_json()
        else:
            return None


async def main():
    endpoint = MyCFXEndpoint("192.168.137.217:12345", "ZKX_MAC")
    container = CFXContainer(endpoint,debug_info=False)
    container.set_heartbeat_frequency(60)

    container.add_publish_channel("192.168.137.1:8888", "event")

    container.open_endpoint()

    # EndpointConnected
    container.publish_msg(
        CFXEnvelope(message_body=EndpointConnected(endpoint.cfx_handle, endpoint.local_url, endpoint.cfx_handle))
    )

    # StationStateChanged
    container.publish_msg(
        CFXEnvelope(message_body=StationStateChanged(old_state_duration="00:05:00",old_state=ResourceState.ENG,new_state=ResourceState.ENG_ProcessExperiments))
    )

    # StationParametersModified
    stationParametersModified = StationParametersModified()
    stationParametersModified.add_modified_parameter(GenericParameter(name="test", value="testValue"))
    container.publish_msg(
        CFXEnvelope(message_body=stationParametersModified)
    )

    # EndpointShuttingDown
    container.publish_msg(
        CFXEnvelope(message_body=EndpointShuttingDown(endpoint.cfx_handle))
    )

    # LogEntryRecorded
    container.publish_msg(
        CFXEnvelope(message_body=LogEntryRecorded("information_id","hah"))
    )


    # StationOnline
    container.publish_msg(
        CFXEnvelope(message_body=StationOnline("00:05:00"))
    )

    # StationOffline
    container.publish_msg(
        CFXEnvelope(message_body=StationOffline())
    )

    # FaultOccurred
    fault = Fault(description="ERROR", fault_code="123")
    fault_occurred = FaultOccurred(fault)
    container.publish_msg(
        CFXEnvelope(message_body=fault_occurred)
    )

    # FaultCleared
    operator_ = Operator()
    fault_cleared = FaultCleared(operator=operator_)
    container.publish_msg(
        CFXEnvelope(message_body=fault_cleared)
    )

    # FaultAcknowledged
    operator = Operator()
    faultAcknowledged = FaultAcknowledged(operator)
    container.publish_msg(
        CFXEnvelope(message_body=faultAcknowledged)
    )


    # RecipeActivate
    container.publish_msg(
        CFXEnvelope(message_body=RecipeActivated(Stage(stageType=StageType.Buffer),"recipe",revision="-1000"))
    )

    # RecipeModified
    container.publish_msg(
        CFXEnvelope(message_body=RecipeModified("recipe", revision="-1000"))
    )

    # unitsArrived
    unitsArrived = UnitsArrived(
        primaryIdentifier="ABC",
        hermesIdentifier="ABCD",
        Lane=1
    )
    unitsArrived.add_units(UnitPosition("a", 2, "A", 1.1, 2.1, 0.5, True, False))

    container.publish_msg(
        CFXEnvelope(message_body=unitsArrived)
    )

    # unitsDeparted
    unitsDeparted = UnitsDeparted(
        primaryIdentifier="ABC",
        hermesIdentifier="ABCD",
        Lane=1
    )
    unitsDeparted.add_units(UnitPosition("a", 2, "A", 1.1, 2.1, 0.5, True, False))
    container.publish_msg(
        CFXEnvelope(message_body=unitsDeparted)
    )

    # WorkCompleted
    workCompleted = WorkCompleted(Result=WorkResult.Failed, primaryIdentifier="AA", hermesIdentifier="BB")
    workCompleted.add_unit(UnitPosition("a", 2, "A", 1.1, 2.1, 0.5, True, False))
    container.publish_msg(CFXEnvelope(message_body=workCompleted))

    # WorkStageCompleted
    workStageCompleted = WorkStageCompleted(stage=Stage(stageName="StageName", stageType=StageType.Work),
                                            result=WorkResult.Skipped)
    container.publish_msg(CFXEnvelope(message_body=workStageCompleted))

    # WorkStagePaused
    workStagePaused = WorkStagePaused(stage=Stage(stageName="StageNameAA", stageType=StageType.Work),
                                      pauseReason=WorkStagePauseReason.Unknown)
    container.publish_msg(CFXEnvelope(message_body=workStagePaused))

    # WorkStageResumed
    workStageResumed = WorkStageResumed(stage=Stage(stageName="StageNameBB",stageType=StageType.Buffer))
    container.publish_msg(CFXEnvelope(message_body=workStageResumed))

    # WorkStageStarted
    workStageStarted = WorkStageStarted(stage=Stage(stageName="StageNameStarted", stageType=StageType.Buffer))
    container.publish_msg(CFXEnvelope(message_body=workStageStarted))

    # WorkStarted
    workStarted = WorkStarted(primaryIdentifier="AAA", hermesIdentifier="BBB")
    workStarted.add_unit(UnitPosition("a", 2, "A", 1.1, 2.1, 0.5, True, False))
    workStarted.add_unit(UnitPosition("a", 2, "A", 1.1, 2.1, 0.5, True, False))
    container.publish_msg(CFXEnvelope(message_body=workStarted))

    # AreYouThereRequest
    response1 = await container.execute_request("192.168.137.1:8888", "PC",
                                                request=CFXEnvelope(message_body=AreYouThereRequest(endpoint.cfx_handle))
                                                )
    if response1:
        print("Response1", response1)
    else:
        print("Response1 time out")

    # WhoIsThereRequest
    whoIsThereRequest = WhoIsThereRequest()
    supportTopic = SupportedTopic(topicName="AAA", topicSupportType=SupportedTopicQueryType.Ignore)
    supportTopic.add_support_message("cvb")
    whoIsThereRequest.add_supported_topic(supportTopic)
    response1 = await container.execute_request("192.168.137.1:8888", "PC",
                                                request=CFXEnvelope(
                                                    message_body=whoIsThereRequest
                                                ))
    if response1:
        print("Response1", response1)
    else:
        print("Response1 time out")

    # GetActiveRecipeRequest
    stage = Stage()
    request = GetActiveRecipeRequest(stage, lane=1)
    response1 = await container.execute_request("192.168.137.1:8888", "PC",
                                                request=CFXEnvelope(
                                                    message_body=request
                                                ))
    if response1:
        print("Response1", response1)
    else:
        print("Response1 time out")

    # ValidateUnitsRequest
    units = [UnitPosition()]
    validateUnitsRequest = ValidateUnitsRequest(primaryIdentifier="aaa", units=units)
    response1 = await container.execute_request("192.168.137.1:8888", "PC",
                                                request=CFXEnvelope(
                                                    message_body=validateUnitsRequest
                                                ))
    if response1:
        print("Response1", response1)
    else:
        print("Response1 time out")

    # container.close_endpoint()


if __name__ == '__main__':
    asyncio.run(main())
