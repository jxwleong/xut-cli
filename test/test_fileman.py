import unittest
import os
import sys

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, ROOT_DIR)

from common.fileman import tuple2list
from common.fileman import remove_dash_in_list
from common.fileman import get_log_timestamp
from common.fileman import log_timestamp_to_integer

class TestCase_tuple2list(unittest.TestCase):
    def test_tuple2list(self):
        list_ = tuple2list([('2021-03-27', '11-12-35-493')])

        self.assertEqual(['2021-03-27', '11-12-35-493'], list_)

class TestCase_remove_dash_in_list(unittest.TestCase):
    def test_remove_dash_in_list(self):
        list_ = remove_dash_in_list(['2021-03-27', '11-12-35-493'])
        
        self.assertEqual(['20210327', '111235493'], list_)
        
class TestCase_get_log_timestamp(unittest.TestCase):
    def test_get_log_timestamp(self):
        tuple_ = get_log_timestamp(
                    log='MonitorLog2021-03-27_19-42-02-296.txt', 
                    pattern='MonitorLog(\\d{4}-\\d{2}-\\d{2})_(\\d{2}-\\d{2}-\\d{2}-\\d{3})'
                    )
        
        self.assertEqual([('2021-03-27', '19-42-02-296')], tuple_)        

class TestCase_log_timestamp_to_integer(unittest.TestCase):
    def test_log_timestamp_to_integer(self):
        timestamp = log_timestamp_to_integer(
                    log='MonitorLog2021-03-27_19-42-02-296.txt'
                    )
        
        self.assertEqual(20210327194202296, timestamp)        

    
if __name__ == '__main__':
    unittest.main()