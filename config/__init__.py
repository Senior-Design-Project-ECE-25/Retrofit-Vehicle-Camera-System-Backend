import os
import json

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
LOG_DIR = BASE_DIR + '/logs'
os.makedirs(LOG_DIR, exist_ok=True)

assert 'config.json' in os.listdir(f'{BASE_DIR}/config/'), \
    'Cannot locate config.json'

with open(f'{BASE_DIR}/config/config.json', 'r') as config_json:
    _config = json.load(config_json)

API_HOST = _config['api']['host']
