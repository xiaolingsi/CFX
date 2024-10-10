import datetime


class CFXUtils:
    @staticmethod
    def get_cfx_version():
        return "python1.0"

    @staticmethod
    def get_iso8601_time():
        return datetime.datetime.now().isoformat()+"+08:00"

