import logging
from logging.handlers import TimedRotatingFileHandler


class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        # 根据日志级别设置颜色
        level = record.levelname
        color = {
            'INFO': Colors.GREEN,
            'WARNING': Colors.YELLOW,
            'ERROR': Colors.RED,
            'CRITICAL': Colors.MAGENTA,
            'DEBUG': Colors.BLUE
        }.get(level, Colors.WHITE)

        # 设置格式化字符串
        format_str = f"{color}%(asctime)s - %(levelname)s - %(message)s{Colors.RESET}"
        self._style._fmt = format_str
        return super().format(record)


class ColoredStreamHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
        self.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s'))


class LogUtils(metaclass=Singleton):
    def __init__(self,file_path=None):
        self.log = logging.getLogger("CFXDemoLogUtils")
        self.log.setLevel(logging.INFO)  # 设置日志级别
        formatter = logging.Formatter('%(asctime)s-%(levelname)s - %(message)s')
        if file_path:
            file_handler = TimedRotatingFileHandler(file_path, when='midnight', interval=1, backupCount=7,
                                                    encoding='utf-8')
            file_handler.setFormatter(formatter)
            self.log.addHandler(file_handler)
        stream_handler = ColoredStreamHandler()
        self.log.addHandler(stream_handler)

    def info_log(self, message):
        self.log.info(message)

    def error_log(self, message):
        self.log.error(message)

    def warning_log(self, message):
        self.log.warning(message)

    def debug_log(self,message):
        self.log.debug(message)

    def critical_log(self,message):
        self.log.critical(message)

