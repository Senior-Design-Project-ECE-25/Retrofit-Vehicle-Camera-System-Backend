import cv2
import time
import logging
import logging.config
import numpy as np
from datetime import timedelta, datetime as dt
try:
    from imutils.video.pivideostream import PiVideoStream
except ImportError:
    PiVideoStream = object()  # For development/testing env

from ...config import LOG_INI_PATH, LOG_DEFAULTS, VIDEO_PATH,\
                      CAMERA_CONF, TIMESTAMP_FORMAT

logging.config.fileConfig(
    LOG_INI_PATH,
    defaults=LOG_DEFAULTS,
    disable_existing_loggers=False
)
vsLogger = logging.getLogger('vsLogger')


class Camera:
    def __init__(self, flip=False, video_stream_cls=PiVideoStream):
        vsLogger.info('Initializing Camera')
        self.video_stream = video_stream_cls(
            resolution=CAMERA_CONF.resolution,
            framerate=CAMERA_CONF.framerate)
        self.video_stream.start()
        time.sleep(2.0)  # Must sleep for cam initialization
        self.flip = flip

        vsLogger.info('Done Initializing Camera')

    def __del__(self):
        self.video_stream.stop()
        self.video_writer.release()

    def frame_generator(self):
        while True:
            frame = self.__get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def record(self):
        last = 0
        frequency = 1 / self.video_stream.camera.framerate
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        while True:
            file = Camera.__generate_file_name()
            video_writer = cv2.VideoWriter(
                file,
                fourcc,
                int(self.video_stream.camera.framerate),
                self.video_stream.camera.resolution
            )

            vsLogger.info(f'Recording Started: {file}')

            end_time = dt.now() + timedelta(minutes=1)
            while dt.now() < end_time:
                while time.time() - last < frequency:
                    time.sleep(0.001)

                frame = self.__read()
                video_writer.write(frame)

            video_writer.release()
            vsLogger.info(f'Recording Finished: {file}')

    def __flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def __read(self):
        frame = self.video_stream.read()
        if self.flip:
            frame = self.__flip_if_needed(frame)
        return frame

    def __get_frame(self):
        frame = self.__read()
        _, jpegFrame = cv2.imencode('.jpg', frame)
        return jpegFrame.tobytes()

    @staticmethod
    def __generate_file_name() -> str:
        ts = dt.now().strftime(TIMESTAMP_FORMAT)
        return VIDEO_PATH + f'/recording-{ts}.mp4'
