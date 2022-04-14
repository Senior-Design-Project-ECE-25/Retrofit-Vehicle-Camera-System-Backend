import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)))
VIDEO_DIR = os.path.join(BASE_DIR, 'videos')
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(VIDEO_DIR, mode=0o777, exist_ok=True)
os.makedirs(LOG_DIR, mode=0o777, exist_ok=True)

CONF_JSON_PATH = os.path.join(BASE_DIR, 'rvcs', 'config', 'conf.json')
LOG_INI_PATH = os.path.join(BASE_DIR, 'rvcs', 'config', 'logger.ini')
assert os.path.exists(CONF_JSON_PATH), \
    f'Cannot locate {CONF_JSON_PATH}'
assert os.path.exists(LOG_INI_PATH), \
    f'Cannot locate {LOG_INI_PATH}'

with open(CONF_JSON_PATH, 'r') as config_json:
    _config = json.load(config_json)

API_HOST = _config['api']['host']
API_PORT = _config['api']['port']

TIMESTAMP_FORMAT = '%Y%m%dT%H%M%S'
