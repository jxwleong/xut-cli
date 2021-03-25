import os
import signal
import subprocess
import psutil
import logging
import sys
import time

import pyautogui
import pygetwindow as gw
import win32gui

ROOT_DIR = os.path.join(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

from image_path import stress_test_image_path
from logger import my_logger

XTU_UI_LAUNCHER_PATH    = r'C:\Program Files\Intel\Intel(R) Extreme Tuning Utility\Client\XtuUiLauncher.exe'
XTU_PROCESS_NAME = 'XtuService.exe'
XTU_WINDOW_NAME = 'eXtreme Tuning Utility'

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

def end_process(pid, signal=signal.SIGTERM):
    logger.info(f'End process with PID: {pid}')
    #os.kill(pid, signal)
    p = psutil.Process(pid)
    p.terminate()

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
        window_found = True
    except IndexError:
        logger.info(f'Cant find window... Wait for 1s')
        time.sleep(1)
        continue

def select_stress_test():
    side_bar_stress_test_image = [stress_test_image_path['stress_unselected'], \
                                  stress_test_image_path['stress_selected']]
    for image in side_bar_stress_test_image:
        if pyautogui.locateOnScreen(image,confidence=0.5, grayscale=True) is not None:
            pyautogui.moveTo(pyautogui.locateCenterOnScreen(image)) 
            pyautogui.leftClick()

# Ref
def killtree(pid, including_parent=False):
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        child.kill()
    if including_parent:
        parent.kill()  ## this program
        
select_stress_test()
xtu_window.activate()
logger.info("Killing XUT now...")
killtree(pid)

