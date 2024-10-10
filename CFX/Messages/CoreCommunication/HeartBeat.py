from CFX.CFXMessage import CFXMessage


class HeartBeat(CFXMessage):
    def __init__(self, cfx_handle, heartbeat_frequency):
        super().__init__()
        self.type = "CFX.Heartbeat,CFX"
        self.message_name = "CFX.Heartbeat"
        self.CFXHandle = cfx_handle
        self.heartbeat_frequency = heartbeat_frequency

    @staticmethod
    def seconds_to_hms(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def to_cfx_json(self):
        return {
            "$type": self.type,
            "CFXHandle": self.CFXHandle,
            "HeartbeatFrequency": HeartBeat.seconds_to_hms(self.heartbeat_frequency),
            "ActiveFaults": None,
            "ActiveRecipes": None
        }
