import abc


class CFXMessage(abc.ABC):
    def __init__(self):
        self.type = "NOT_SET_ERROR"
        self.message_name = "NOT_SET_ERROR"

    @abc.abstractmethod
    def to_cfx_json(self):
        pass
