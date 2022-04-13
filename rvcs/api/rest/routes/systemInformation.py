from flask import jsonify
from flask_restful import Resource
from subprocess import check_output

from ..utilities.utils import log_request


class SystemInformation(Resource):
    endpoint = '/api/v1/SystemInformation'

    def __init__(self) -> None:
        super(SystemInformation, self).__init__()

    @log_request
    def get(self):
        return jsonify(data={
            'os-info': System.get_os_information(),
            'rvcs-version': System.get_rvcs_version(),
            'bt-mac': System.get_bluetooth_mac()
        })


class System:
    """Collection of system information getters."""
    def __init__(self) -> None:
        print('Not meant to be instantiated.')

    @staticmethod
    def get_os_information() -> dict:
        raw = check_output(['cat', '/etc/os-release'])\
                           .decode('utf-8')
        info_pairs = [kv.split('=') for kv in raw.split('\n')]
        return {
            pair[0]: pair[1]
            for pair in info_pairs
            if len(pair) == 2
        }

    @staticmethod
    def get_rvcs_version() -> str:
        return 'v1.0.0 beta'

    @staticmethod
    def get_bluetooth_mac() -> str:
        raw = check_output(['sudo', 'ls', '/var/lib/bluetooth/'])\
                           .decode('utf-8')
        return raw.split('\n')[0]


if __name__ == '__main__':
    print(System.get_os_information())
    print(System.get_rvcs_version())
    print(System.get_bluetooth_mac())
