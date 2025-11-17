from CFX.CFXMessage import CFXMessage
from CFX.Messages.genericUnits.StatusResult import StatusResult
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RequestResult(CFXMessage):
    Result:StatusResult
    ResultCode:int
    Message:str

    def __init__(self, result: StatusResult, result_code, message):
        super().__init__()
        self.Result: StatusResult = result
        self.ResultCode = result_code
        self.Message = message

    def to_cfx_json(self):
        return {
            "Result": str(self.Result).split(".")[1],
            "ResultCode": self.ResultCode,
            "Message": self.Message
        }

    def to_json(self):
        return {
            "Result": str(self.Result).split(".")[1],
            "ResultCode": self.ResultCode,
            "Message": self.Message
        }
