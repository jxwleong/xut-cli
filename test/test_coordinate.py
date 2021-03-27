import unittest
import os
import sys

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, ROOT_DIR)

from common.coordinate import Coordinate
from common.coordinate import get_active_button_coordinate

class TestCase_get_active_button_coordinate(unittest.TestCase):
    def test_get_active_button_coordinate_given_window_coordinate_x0_y0(self):
        window_coordinate = Coordinate(0, 0)
        button_coordinate = get_active_button_coordinate(window_coordinate, 'TOP_BAR')
        #   X    Y
        # (365, 20)
        self.assertEqual(365, button_coordinate.x)
        self.assertEqual(20, button_coordinate.y)


if __name__ == '__main__':
    unittest.main()