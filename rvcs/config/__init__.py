import os
import json

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)))
VIDEO_PATH = os.path.join(BASE_PATH, 'videos')
os.makedirs(VIDEO_PATH, mode=0o777, exist_ok=True)
LOG_PATH = os.path.join(BASE_PATH, 'logs')
os.makedirs(LOG_PATH, mode=0o777, exist_ok=True)

LOG_INI_PATH = os.path.join(BASE_PATH, 'rvcs', 'config', 'logger.ini')
assert os.path.exists(LOG_INI_PATH), f'Cannot locate {LOG_INI_PATH}'

LOG_DEFAULTS = {
    'vsLogFileName': os.path.join(LOG_PATH, 'vs.log'),
    'appLogFileName': os.path.join(LOG_PATH, 'app.log')
}

CONF_JSON_PATH = os.path.join(BASE_PATH, 'rvcs', 'config', 'conf.json')
assert os.path.exists(CONF_JSON_PATH), f'Cannot locate {CONF_JSON_PATH}'

with open(CONF_JSON_PATH, 'r') as config_json:
    _config = json.load(config_json)

API_HOST = _config['api']['host']
API_PORT = _config['api']['port']
CAMERA_FRAMERATE = _config['camera']['framerate']
CAMERA_RESOLUTION = tuple(_config['camera']['resolution'])

TIMESTAMP_FORMAT = '%Y%m%dT%H%M%S'
