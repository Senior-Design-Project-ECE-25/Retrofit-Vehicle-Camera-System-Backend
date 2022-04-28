import logging
import logging.config
from typing import Any, Callable, Dict, Tuple

from ....config import LOG_INI_PATH, LOG_DEFAULTS

logging.config.fileConfig(
    LOG_INI_PATH,
    defaults=LOG_DEFAULTS,
    disable_existing_loggers=False
)
appLogger = logging.getLogger('appLogger')


def log_request(func) -> Callable:
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
        try:
            ret = func(*args, **kwargs)
            appLogger.info(f'{func.__qualname__} successful')
            return ret
        except Exception as err:
            appLogger.error(f'{func.__qualname__} failed - {err}')
    return wrapper
