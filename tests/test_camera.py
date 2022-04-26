import numpy as np
import unittest
from unittest.mock import Mock

from .context import Camera


def create_PiVideoStream_mock():
    pvs_mock = Mock()
    pvs_mock.return_value.camera.resolution = (320, 480)
    pvs_mock.return_value.camera.framerate = 32
    pvs_mock.return_value.read.return_value = np.zeros(shape=(1, 1))
    pvs_mock.return_value.start.return_value = None
    pvs_mock.return_value.release.return_value = None
    return pvs_mock


class TestCamera(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pvs_mock = create_PiVideoStream_mock()
        cls.camera = Camera(video_stream_cls=pvs_mock)

    def setUp(self):
        self.camera = TestCamera.camera

    def test_frame_generator(self):
        for frame in self.camera.frame_generator():
            self.assertIsInstance(frame, bytes)
            break  # only need to test one frame

    def test_record(self):
        pass


if __name__ == '__main__':
    unittest.main()
