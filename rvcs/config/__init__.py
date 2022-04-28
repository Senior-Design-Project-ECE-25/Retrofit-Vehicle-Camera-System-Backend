import os
import json
from dataclasses import dataclass
from typing import Tuple


@dataclass
class ApiConfig:
    host: str
    port: int


@dataclass
class CameraConfig:
    width: int
    height: int
    framerate: int

    @property
    def resolution(self) -> Tuple[int]:
        return (self.width, self.height)


BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
VIDEO_PATH = os.path.join(BASE_PATH, 'videos')
LOG_PATH = os.path.join(BASE_PATH, 'logs')

os.makedirs(VIDEO_PATH, mode=0o777, exist_ok=True)
os.makedirs(LOG_PATH, mode=0o777, exist_ok=True)

LOG_INI_PATH = os.path.join(BASE_PATH, 'config', 'logger.ini')
assert os.path.exists(LOG_INI_PATH), f'Cannot locate {LOG_INI_PATH}'

LOG_DEFAULTS = {
    'vsLogFileName': os.path.join(LOG_PATH, 'vs.log'),
    'appLogFileName': os.path.join(LOG_PATH, 'app.log')
}

CONF_JSON_PATH = os.path.join(BASE_PATH, 'config', 'conf.json')
assert os.path.exists(CONF_JSON_PATH), f'Cannot locate {CONF_JSON_PATH}'

with open(CONF_JSON_PATH, 'r') as config_json:
    _config = json.load(config_json)

API_CONF = ApiConfig(**_config['api'])
CAMERA_CONF = CameraConfig(**_config['camera'])

TIMESTAMP_FORMAT = '%Y%m%dT%H%M%S'
