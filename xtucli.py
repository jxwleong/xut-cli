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

from image_path import stress_test_image_path
from logger import my_logger
from common.CONSTANT import *
from common.coordinate import Coordinate
from common.coordinate import calculate_active_button_coordinate
import process as ps
import arg_parse

logger = logging.getLogger(__name__)


if ps.is_xtu_running() is True:
    logger.info(f'XTU is already running, kill all xtu process now...')
    ps.kill_all_xtu_process()

logger.info('XTU process not found, launching now...')
proc = subprocess.Popen(XTU_UI_LAUNCHER_PATH)
time.sleep(5)
pid = ps.get_process_pid(XTU_PROCESS_NAME)
logger.info(f'XTU is launched with PID: {pid}')
logger.info(f'{ps.get_all_xtu_process()}')
window_found = False
count = 0
while window_found is False:

    try:
        xtu_window = gw.getWindowsWithTitle(XTU_WINDOW_NAME)[0]
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

window_coordiate = Coordinate(xtu_window.left, xtu_window.top)

# if xtu_window.isMaximized is True:
#     pyautogui.click(x+331, y+14, clicks=2)
# pyautogui.click(x + 63, y + 205)
# time.sleep(1)
# pyautogui.click(x + 243, y + 129)
# time.sleep(1)
# # Days
# #pyautogui.click("left",x + 558, y + 133)
# pyautogui.click(x + 755, y + 135)
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.click(x + 303, y + 331)



ps.kill_all_xtu_process()
# kill_process_with_pid(pid)
# kill_process_with_pid(proc.pid)
# kill_process_with_pid(get_process_pid('PerfTune.exe'))