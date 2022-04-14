import unittest
from unittest.mock import Mock

from .context import Camera


class TestCamera(unittest.TestCase):
    def setUp(self):
        video_module_mock = Mock()
        video_module_mock.return_value.resolution = (320, 480)
        video_module_mock.return_value.framerate = 32
        self.camera = Camera(video_module=video_module_mock)

    def test_frame_generator(self):
        pass

    def test_record(self):
        pass


if __name__ == '__main__':
    unittest.main()
