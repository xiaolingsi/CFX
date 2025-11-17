import abc


class CFXMessageImplements(abc.ABC):
    @abc.abstractmethod
    def on_message_receive_from_listener(self, msg) -> None:
        pass

    @abc.abstractmethod
    def on_request_receive(self, request) -> [dict, None]:
        pass
