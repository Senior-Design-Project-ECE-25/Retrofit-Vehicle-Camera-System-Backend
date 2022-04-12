import threading
from flask import Flask
from flask_restful import Api

from api.services.camera import VideoCamera
from api.rest.routes import Logs, Index, VideoFeed, SystemInformation


class RVCSApp:
    def __init__(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        self.camera = VideoCamera()

        api.add_resource(Logs, Logs.endpoint)
        api.add_resource(Index, Index.endpoint)
        videoFeedApi = VideoFeed.instantiate_camera(self.camera)
        api.add_resource(videoFeedApi, videoFeedApi.endpoint)
        api.add_resource(SystemInformation, SystemInformation.endpoint)

    def run(self, host, port):
        recording_thread = threading.Thread(target=self.camera.record())
        recording_thread.start()
        self.app.run(host=host, port=port)


if __name__ == '__main__':
    from api.config import API_HOST, API_PORT
    RVCSApp().run(host=API_HOST, port=API_PORT)
