import cv2
import time
import logging
import logging.config
import numpy as np
from datetime import datetime as dt
from imutils.video.pivideostream import PiVideoStream

from ...config import BASE_DIR, VIDEO_DIR, TIMESTAMP_FORMAT

logging.config.fileConfig(f'{BASE_DIR}/api/config/logger.ini',
                          disable_existing_loggers=False)
vsLogger = logging.getLogger('vsLogger')


class VideoCamera:
    def __init__(self, flip=False):
        vsLogger.info('Initializing Camera')
        self.video_stream = PiVideoStream().start()
        time.sleep(2.0)  # Must sleep for cam initialization
        self.flip = flip

        file = VideoCamera.__generate_file_name()
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(
            file,
            fourcc,
            self.video_stream.framerate,
            self.video_stream.resolution
        )

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
        frequency = 1 / self.video_stream.framerate

        while True:
            while time.time() - last < frequency:
                time.sleep(0.001)
            frame = self.__read()
            self.video_writer.write(frame)

    def __get_frame(self):
        frame = self.__read()
        _, jpegFrame = cv2.imencode('.jpg', frame)
        return jpegFrame.tobytes()

    def __read(self):
        frame = self.video_stream.read()
        if self.flip:
            frame = self.__flip_if_needed(frame)
        return frame

    def __flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    @staticmethod
    def __generate_file_name() -> str:
        ts = dt.now().strftime(TIMESTAMP_FORMAT)
        return VIDEO_DIR + f'/recording-{ts}.mp4'
