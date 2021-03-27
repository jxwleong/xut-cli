import logging
import time
import os
import sys
import psutil
import subprocess

import pyautogui


ROOT_DIR = os.path.join(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from logger import my_logger
from common.CONSTANT import *
from common.coordinate import Coordinate
from common.coordinate import get_active_button_coordinate
import process as ps
import arg_parse
import interfacer as i

logger = logging.getLogger(__name__)


if ps.is_xtu_running() is True:
    logger.info(f'XTU is already running, kill all xtu process now...')
    ps.kill_all_xtu_process()

logger.info('XTU process not found, launching now...')
proc = subprocess.Popen(XTU_UI_LAUNCHER_PATH)
time.sleep(5)
pid = ps.get_process_pid(XTU_PROCESS_NAME)

xtu_window = i.activate_window()
window_coordinate = Coordinate(xtu_window.left, xtu_window.top)

start = time.time()
end = start + DEFAULT_STRESS_TEST_TIME*60

if xtu_window.isMaximized is True:
    i.click(window_coordinate, button='TOP_BAR' ,clicks=2, interval=0.2)
    xtu_window = i.activate_window()
    window_coordinate = Coordinate(xtu_window.left, xtu_window.top)
i.click(window_coordinate, button='STRESS_TEST_SIDEBAR')
i.click(window_coordinate, button='STRESS_TEST_CPU_CHECKBOX')

i.click(window_coordinate, button='START_TESTING')
i.click(window_coordinate, button='FILE_LOGGING')

loop=0
while time.time() < end:
    if time.time()- (60*loop) > start+60: 
        logger.info(f"Start time: {time.strftime('%d/%m/%y %H:%M:%S', time.gmtime(start))} "\
                    f"Current time: {time.strftime('%d/%m/%y %H:%M:%S', time.gmtime(time.time()))} ")
        loop += 1
i.click(window_coordinate, button='FILE_LOGGING')
i.click(window_coordinate, button='STOP_TESTING')
logger.info(f'Check log file at: C:\ProgramData\Intel\Intel Extreme Tuning Utility\Monitor Logs')
    
ps.kill_all_xtu_process()
