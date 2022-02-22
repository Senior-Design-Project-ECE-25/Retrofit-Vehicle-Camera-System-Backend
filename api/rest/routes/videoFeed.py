from flask import Response, jsonify
from flask_restful import Resource, Api

from ...services.camera import VideoCamera
from ..utilities.utils import log_request


class VideoFeed(Resource):
    endpoint = '/api/v1/VideoFeed'

    def __init__(self) -> None:
        super(VideoFeed, self).__init__()

    @log_request
    def get(self) -> Response:
        return Response(
            self.camera.frame_generator(),
            mimetype='multipart/x-mixed-replace; boundary=frame'
        )

    @classmethod
    def instantiate_camera(cls, camera) -> None:
        cls.camera = camera
        return cls
