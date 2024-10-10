import uuid

from CFX.CFXMessage import CFXMessage
from CFX.CFXUtils import CFXUtils


class CFXEnvelope(object):

    def __init__(self, source="", target="", request_id="", message_body: CFXMessage = None):
        self.Version = CFXUtils.get_cfx_version()
        self.MessageName = "" if not message_body else message_body.message_name
        self.Source = source
        self.Target = target
        self.RequestID = request_id if request_id else str(uuid.uuid4())
        self.TimeStamp = CFXUtils.get_iso8601_time()
        self.UniqueID = str(uuid.uuid4())
        self.MessageBody: CFXMessage = message_body

    @property
    def version(self):
        return self.Version

    @version.setter
    def version(self, value):
        raise Exception("Version is read only")

    def to_json(self):
        return {
            "MessageName": self.MessageName,
            "Version": self.Version,
            "TimeStamp": self.TimeStamp,
            "UniqueID": self.UniqueID,
            "Source": self.Source,
            "Target": self.Target,
            "RequestID": self.RequestID,
            "MessageBody": self.MessageBody.to_cfx_json()
        }
