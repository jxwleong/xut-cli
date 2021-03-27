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

XTU_UI_LAUNCHER_PATH    = r'C:\Program Files\Intel\Intel(R) Extreme Tuning Utility\Client\XtuUiLauncher.exe'
XTU_WINDOW_TITLE = 'Intel® Extreme Tuning Utility'
XTU_WINDOW_NAME = 'eXtreme Tuning Utility'
XTU_PROCESS_NAME = 'XtuService.exe'

logger = logging.getLogger(__name__)

def get_process_pid(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return proc.pid

def is_process_running(process_name):
    # source: https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

if is_process_running(XTU_PROCESS_NAME) is False:
    logger.info('XTU process not found, launching now...')
    proc = subprocess.Popen(XTU_UI_LAUNCHER_PATH)
    time.sleep(5)
    pid = get_process_pid(XTU_PROCESS_NAME)
    logger.info(f'XTU is launched with PID: {pid}')
else:
    pid = get_process_pid(XTU_PROCESS_NAME)
    logger.info(f'XTU is already running with PID: {pid}')


window_found = False
while window_found is False:
    try:
        xtu_window = gw.getWindowsWithTitle(XTU_WINDOW_NAME)[0]
        logger.info(f'Window: {xtu_window}')
        xtu_window.activate()
        time.sleep(1)
        window_found = True
    except IndexError:
        logger.info(f'Cant find window... Wait for 1s')
        time.sleep(1)
        continue

x = xtu_window.left
y = xtu_window.top


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

os.system(f'taskkill /F /PID {pid}')
os.system(f'taskkill /F /PID {proc.pid}')
os.system(f"taskkill /F /PID {get_process_pid('PerfTune.exe')}")