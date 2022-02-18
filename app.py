from flask import Flask, render_template, Response, jsonify
from flask_restful import Resource, Api, reqparse

from classes.camera import VideoCamera
from utils import log_request
from config import API_HOST, API_PORT

camera = VideoCamera()

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    endpoint = '/'

    def __init__(self):
        super(Index, self).__init__()

    @log_request
    def get(self):
        return render_template('index.html')


api.add_resource(Index, Index.endpoint)


class VideoFeed(Resource):
    endpoint = '/api/v1/VideoFeed'

    def __init__(self):
        super(VideoFeed, self).__init__()

    @log_request
    def get(self):
        return Response(
            camera.frame_generator(),
            mimetype='multipart/x-mixed-replace; boundary=frame'
        )


api.add_resource(VideoFeed, VideoFeed.endpoint)


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)
