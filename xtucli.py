import logging
import time
import os
import sys
import psutil
import subprocess

import pyautogui
import pygetwindow as gw

ROOT_DIR = os.path.join(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from logger import my_logger
from common.CONSTANT import *
from common.coordinate import Coordinate
from common.coordinate import get_active_button_coordinate
import process as ps
import arg_parse
import clicker as c

logger = logging.getLogger(__name__)


if ps.is_xtu_running() is True:
    logger.info(f'XTU is already running, kill all xtu process now...')
    ps.kill_all_xtu_process()

logger.info('XTU process not found, launching now...')
proc = subprocess.Popen(XTU_UI_LAUNCHER_PATH)
time.sleep(5)
pid = ps.get_process_pid(XTU_PROCESS_NAME)
window_found = False
count = 0
while window_found is False:

    try:
        xtu_window = gw.getWindowsWithTitle(XTU_WINDOW_NAME)[0]
        logger.info(f'XTU window found!')
        logger.info(f'Window: {xtu_window}')
        xtu_window.activate()
        time.sleep(1)
        window_found = True
    except IndexError:
        logger.info(f'Grabbing XTU window, retries({count}/5)')
        count += 1
        time.sleep(5)
        continue
time.sleep(1)

window_coordinate = Coordinate(xtu_window.left, xtu_window.top)

if xtu_window.isMaximized is True:
    c.click(window_coordinate, button='TOP_BAR' ,clicks=2)
c.click(window_coordinate, button='STRESS_TEST_SIDEBAR')
c.click(window_coordinate, button='STRESS_TEST_CPU_CHECKBOX')

c.click(window_coordinate, button='START_TESTING')
c.click(window_coordinate, button='FILE_LOGGING')


time.sleep(10)
c.click(window_coordinate, button='FILE_LOGGING')
c.click(window_coordinate, button='STOP_TESTING')
logger.info(f'Check log file at: C:\ProgramData\Intel\Intel Extreme Tuning Utility\Monitor Logs')
time.sleep(2)
ps.kill_all_xtu_process()
