import logging
import logging.config

from config import BASE_DIR

logging.config.fileConfig(f'{BASE_DIR}/config/logger.ini',
                          disable_existing_loggers=False)
appLogger = logging.getLogger('appLogger')


def log_request(func):
    def wrapper(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
            appLogger.info('Index.get successful')
            return ret
        except Exception as err:
            appLogger.error(f'Index.get failed - {err}')
    return wrapper
