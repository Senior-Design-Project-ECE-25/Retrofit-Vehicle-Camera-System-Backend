import logging
import logging.config
from flask import Flask, render_template, Response, request

from classes.camera import VideoCamera
from config import API_HOST, BASE_DIR

logging.config.fileConfig(f'{BASE_DIR}/config/logger.ini',
                          disable_existing_loggers=False)
appLogger = logging.getLogger('appLogger')

pi_camera = VideoCamera()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    appLogger.info('Opening Video Stream Connection')
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host=API_HOST)
