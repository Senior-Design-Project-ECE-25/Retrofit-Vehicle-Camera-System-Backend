import logging
import logging.config

from ...config import BASE_DIR

logging.config.fileConfig(f'{BASE_DIR}/api/config/logger.ini',
                          disable_existing_loggers=False)
appLogger = logging.getLogger('appLogger')


def log_request(func):
    def wrapper(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
            appLogger.info(func.__qualname__)
            return ret
        except Exception as err:
            appLogger.error(func.__qualname__)
    return wrapper
