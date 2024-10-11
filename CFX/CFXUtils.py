import datetime
import logging
import os.path
from logging.handlers import TimedRotatingFileHandler

GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
END_COLOR = '\033[0m'


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt, datefmt)
        self.color_map = {
            logging.DEBUG: GREEN,
            logging.INFO: GREEN,
            logging.WARNING: ORANGE,
            logging.ERROR: RED,
            logging.CRITICAL: RED,
        }

    def format(self, record):
        color = self.color_map.get(record.levelno, '')
        formatted_message = super().format(record)
        return f"{color}{formatted_message}{END_COLOR}"


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CFXUtils(metaclass=Singleton):
    @staticmethod
    def get_cfx_version():
        return "python1.0"

    @staticmethod
    def get_iso8601_time():
        return datetime.datetime.now().isoformat() + "+08:00"

    def __init__(self, logging_level=logging.INFO):
        self.log = logging.getLogger("CFXUtils")
        self.log.setLevel(logging_level)
        formatter = ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.log.addHandler(stream_handler)

    def info_log(self, message):
        self.log.info(message)

    def error_log(self, message):
        self.log.error(message)

    def warning_log(self, message):
        self.log.warning(message)

    def set_log_path(self,log_path):
        if log_path:
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler = TimedRotatingFileHandler(os.path.join(log_path, 'CFXLog'),
                                                    when='midnight',
                                                    interval=1,
                                                    backupCount=7,
                                                    encoding='utf-8')
            file_handler.setFormatter(formatter)
            self.log.addHandler(file_handler)


