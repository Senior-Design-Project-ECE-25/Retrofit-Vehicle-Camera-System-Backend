import logging
import logging.config

from ...config import LOG_INI_PATH

logging.config.fileConfig(LOG_INI_PATH, disable_existing_loggers=False)
appLogger = logging.getLogger('appLogger')


def log_request(func):
    def wrapper(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
            appLogger.info(f'{func.__qualname__} successful')
            return ret
        except Exception as err:
            appLogger.error(f'{func.__qualname__} failed - {err}')
    return wrapper
