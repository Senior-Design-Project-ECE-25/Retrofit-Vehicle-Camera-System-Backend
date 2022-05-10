import os
from flask import abort, jsonify, Response
from flask_restful import Resource

from ....config import VIDEO_PATH
from ..utilities.utils import log_request


class Videos(Resource):
    endpoint = '/api/v1/Videos'

    def __init__(self) -> None:
        super(Videos, self).__init__()

    @log_request
    def get(self) -> Response:
        return jsonify(
            data=[
                video_file for video_file in os.listdir(VIDEO_PATH)
                if video_file.endswith('.mp4')
            ]
        )

    @log_request
    def post(self, video_file: str) -> Response:
        if video_file not in os.listdir(VIDEO_PATH):
            abort(404)

        return jsonify(data=video_file)
