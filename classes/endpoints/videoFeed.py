from flask import Response, jsonify
from flask_restful import Resource, Api

from classes.camera import VideoCamera
from utils import log_request


class VideoFeed(Resource):
    endpoint = '/api/v1/VideoFeed'

    def __init__(self) -> None:
        self.camera = VideoCamera()
        super(VideoFeed, self).__init__()

    @log_request
    def get(self) -> Response:
        return Response(
            self.camera.frame_generator(),
            mimetype='multipart/x-mixed-replace; boundary=frame'
        )
        return jsonify('VideoFeed Endpoint')
