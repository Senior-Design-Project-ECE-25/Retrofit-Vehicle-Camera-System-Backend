import os
from flask import abort, jsonify, Response
from flask_restful import Resource

from ....config import VIDEO_PATH
from ..utilities.utils import log_request


class Video(Resource):
    endpoint = '/api/v1/Video/{}'

    def __init__(self) -> None:
        super(Video, self).__init__()

    @log_request
    def get(self, video_file: str) -> Response:
        if video_file not in os.listdir(VIDEO_PATH):
            abort(404)

        return jsonify(data=video_file)


class VideoList(Resource):
    endpoint = '/api/v1/VideoList'

    def __init__(self) -> None:
        super(VideoList, self).__init__()

    @log_request
    def get(self) -> Response:
        return jsonify(
            data=[
                video_file for video_file in os.listdir(VIDEO_PATH)
                if video_file.endswith('.mp4')
            ]
        )
