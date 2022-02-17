import cv2
import time
import logging
import logging.config
import numpy as np
from imutils.video.pivideostream import PiVideoStream

from config import BASE_DIR

logging.config.fileConfig(f'{BASE_DIR}/config/logger.ini',
                          disable_existing_loggers=False)
vsLogger = logging.getLogger('vsLogger')


class VideoCamera:
    def __init__(self, flip=False):
        vsLogger.info('Initializing Camera')
        self.videoStream = PiVideoStream().start()
        self.flip = flip
        time.sleep(2.0)
        vsLogger.info('Done Initializing Camera')

    def __del__(self):
        self.videoStream.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.videoStream.read()
        if self.flip:
            frame = self.flip_if_needed(frame)

        _, jpegFrame = cv2.imencode('.jpg', frame)
        return jpegFrame.tobytes()
