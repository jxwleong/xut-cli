import unittest
import os
import sys

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, ROOT_DIR)

from common.fileman import tuple2list
from common.fileman import remove_dash_in_list

class TestCase_tuple2list(unittest.TestCase):
    def test_tuple2list(self):
        list_ = tuple2list([('2021-03-27', '11-12-35-493')])

        self.assertEqual(['2021-03-27', '11-12-35-493'], list_)

class TestCase_remove_dash_in_list(unittest.TestCase):
    def test_remove_dash_in_list(self):
        list_ = remove_dash_in_list(['2021-03-27', '11-12-35-493'])
        
        self.assertEqual(['20210327', '111235493'], list_)
        
if __name__ == '__main__':
    unittest.main()