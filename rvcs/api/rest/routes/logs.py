import os
from typing import Dict
from flask import Response, jsonify
from flask_restful import Resource

from ....config import LOG_PATH
from ..utilities.utils import log_request


class Logs(Resource):
    endpoint = '/api/v1/logs'
    log_files = ['app.log', 'vs.log']

    def __init__(self) -> None:
        super(Logs, self).__init__()

    @log_request
    def get(self) -> Response:
        data = {}
        for log in self.log_files:
            filename = os.path.splitext(log)[-2]
            data[filename] = []

            with open(os.path.join(LOG_PATH, log), 'r') as log_data:
                tmp = []
                for line in log_data:
                    tmp.append(self.__format_log_line(line))
                data[filename] = tmp[-25:]

        return jsonify(data=data)

    @staticmethod
    def __format_log_line(line: str) -> Dict[str, str]:
        delimiter = ' | '
        ts, ctxt, lvl, mes = line.strip().split(delimiter)
        return {
            'timestamp': ts,
            'context': ctxt,
            'level': lvl,
            'message': mes
        }
