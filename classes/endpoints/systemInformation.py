from flask import jsonify
from flask_restful import Resource
from subprocess import check_output

from utils import log_request


class SystemInformation(Resource):
    endpoint = '/api/v1/SystemInformation'

    def __init__(self) -> None:
        super(SystemInformation, self).__init__()

    @log_request
    def get(self):
        return jsonify(data={
            'osVersion': check_output(['cat', '/etc/os-release'])
            .decode('utf-8'),
            'rvcsVersion': 'v1.0.0 beta'
        })
