import logging
import logging.config
from flask import Flask, render_template, Response, request, jsonify
from flask_restful import Resource, Api, reqparse

from classes.camera import VideoCamera
from config import API_HOST, API_PORT, BASE_DIR

logging.config.fileConfig(f'{BASE_DIR}/config/logger.ini',
                          disable_existing_loggers=False)
appLogger = logging.getLogger('appLogger')

pi_camera = VideoCamera()

app = Flask(__name__)
api = Api(app)


def frame_generator(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


class Index(Resource):
    endpoint = '/'

    def __init__(self):
        super(Index, self).__init__()

    def get(self):
        try:
            payload = render_template('index.html')
            appLogger.info('Index.get successful')
            return payload
        except Exception as err:
            appLogger.error(f'Index.get failed - {err}')


api.add_resource(Index, Index.endpoint)


class VideoFeed(Resource):
    endpoint = '/api/v1/VideoFeeds'

    def __init__(self):
        super(VideoFeed, self).__init__()

    def get(self):
        try:
            payload = Response(
                frame_generator(pi_camera),
                mimetype='multipart/x-mixed-replace; boundary=frame'
            )
            appLogger.info('VideoFeed.get successful')
            return payload
        except Exception as err:
            appLogger.error(f'VideoFeed.get failed - {err}')


api.add_resource(VideoFeed, VideoFeed.endpoint)


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)
