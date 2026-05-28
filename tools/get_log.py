import logging.handlers
import os
from config import BASE_PATH


class GetLog:
    __logger = None

    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            cls.__logger = logging.getLogger()
            cls.__logger.setLevel(logging.INFO)
            log_path = os.path.join(BASE_PATH, "logs", "hmtt.log")
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            th = logging.handlers.TimedRotatingFileHandler(
                filename=log_path,
                when="midnight",
                interval=1,
                backupCount=3,
                encoding="utf-8"
            )
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            th.setFormatter(fm)
            cls.__logger.addHandler(th)
        return cls.__logger


if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info("测试信息级别日志")
