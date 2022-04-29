import threading
from flask import Flask
from flask_restful import Api

from .config import API_CONF
from .api.services.camera import Camera
from .api.rest.routes import Logs, Index, SystemInformation, \
                             VideoFeed, VideoFeedFlex


class App:
    def __init__(self) -> None:
        self.app = Flask(__name__)
        api = Api(self.app)
        self.camera = Camera()

        api.add_resource(Logs, Logs.endpoint)
        api.add_resource(Index, Index.endpoint)
        VideoFeedWithCamera = VideoFeed.attach_camera(self.camera)
        api.add_resource(VideoFeedWithCamera, VideoFeedWithCamera.endpoint)
        api.add_resource(VideoFeedFlex, VideoFeedFlex.endpoint)
        api.add_resource(SystemInformation, SystemInformation.endpoint)

    def run(self, host=API_CONF.host, port=API_CONF.port) -> None:
        recording_thread = threading.Thread(target=self.camera.record)
        recording_thread.start()
        self.app.run(host=host, port=port)
